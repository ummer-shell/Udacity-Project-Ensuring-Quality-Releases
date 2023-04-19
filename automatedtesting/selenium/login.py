# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging

def logging_config():
    """Configure logger"""

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename='ui-test-log.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d%m%y %H:%M:%S',
        level=logging.INFO
    )
    
    return

def printlog(logging_str):
    print(logging_str)
    logging.info(logging_str)
    return

def start_browser():
    """Start the browser."""
    printlog('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    printlog('Browser started successfully.')

    return driver


def login(driver, user, password):
    """Navigate to the page and Login with standard_user."""
    printlog('Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    printlog(f"Logging in with {user}")

    # Set login input values as user and password
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)

    # retirieve login button and click
    driver.find_element(By.ID, "login-button").click()
    
    # log statement
    printlog(f"Logged in with {user}")

    return


def add_items_to_cart(driver):
    """Add items to cart and print."""
    printlog("Adding 6 items to cart")
    # locate items
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Loop over all items and add to cart
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item.find_element(By.TAG_NAME, "button").click()
        printlog(f"{item_name} added to cart")
    
    # Verify that 6 itemsare added to the cart
    num_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert num_cart == '6'
    printlog("Verified 6 items added to cart")
    


def remove_items_from_cart(driver):
    """Remove items to cart and print."""
    printlog("Navigating to cart")

    # Click on shopping cart link
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # locate items
    items = driver.find_elements(By.CLASS_NAME, "cart_item")

    # Verify still 6 items in the cart
    assert len(items) == 6
    printlog("Verified 6 items are in cart")

    # Loop over all items and remove from cart
    printlog("Removing 6 items from cart")
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item.find_element(By.TAG_NAME, "button").click()
        printlog(f"{item_name} removed from cart")

    # Verify no remaining items in cart
    remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(remaining_items) == 0
    printlog("Verified 0 items remain in cart")

if __name__ == "__main__":
    printlog("======================================")

    logging_config()
    driver = start_browser()
    login(driver, 'standard_user', 'secret_sauce')
    add_items_to_cart(driver)
    remove_items_from_cart(driver)
    printlog("End of test.")

    printlog("======================================")
