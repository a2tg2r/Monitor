import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# List of accounts (replace with actual usernames and passwords)
accounts = [
    {"username": "KiwiSubZeroPTG", "password": "14670qeyip"},
    {"username": "Farmerinmm29", "password": "1234567890qeyip"},
    {"username": "Farmermm2299", "password": "1234567890qeyip"},
    {"username": "M2farm8", "password": "101113LK"},
    {"username": "10farm18", "password": "101113LK"},
    {"username": "Mm2craxyfarm0", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm01", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm02", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm03", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm5", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm11", "password": "1234567890qeyip"}
]

# Function to create a headless Chrome driver
def create_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Disable the sandbox for headless mode
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Function to log into Roblox
def roblox_login(driver, username, password):
    login_url = "https://www.roblox.com/login"
    driver.get(login_url)
    time.sleep(3)  # Wait for the page to load
    
    # Find and fill the login form
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

# Function to visit the friend's profile and join the game
def visit_profile_and_join(driver):
    # URL of the friend's profile to join the game (Iz9vs2k)
    friend_profile_url = "https://www.roblox.com/users/1759864847/profile"
    
    # Navigate to the profile URL
    driver.get(friend_profile_url)
    time.sleep(3)  # Wait for the page to load

    # Find the "Join" button (adjust the XPATH or class if necessary)
    try:
        join_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Join')]")
        join_button.click()
        print("Joined the game successfully!")
    except Exception as e:
        print(f"Error joining game: {e}")

# Main function to run the script
def main():
    for account in accounts:
        # Create the driver for each account
        print(f"Logging in with account: {account['username']}")
        driver = create_driver()

        # Log into Roblox with the current account
        roblox_login(driver, account['username'], account['password'])

        # Visit the profile and join the game
        visit_profile_and_join(driver)

        # Keep the session open forever to remain AFK
        print(f"Account {account['username']} is now AFK indefinitely...")
        
        # Keep the session alive by having an infinite loop that does nothing
        while True:
            time.sleep(60)  # Sleep for 1 minute to avoid overloading the CPU

        # Quit the driver after finishing the session (won't be reached in the current logic)
        driver.quit()

if __name__ == "__main__":
    main()
