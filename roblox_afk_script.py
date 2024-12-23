import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION --- #
ACCOUNTS = [
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

PROFILE_URL = "https://www.roblox.com/users/1759864847/profile"  # Iz9vs2k's Profile URL

# --- FUNCTION TO LOG IN TO ROBLOX --- #
def roblox_login(driver, account):
    driver.get('https://www.roblox.com/login')

    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    username_field.send_keys(account['username'])
    password_field.send_keys(account['password'])

    # Click login button
    login_button = driver.find_element(By.XPATH, '//button[@data-testid="login-button"]')
    login_button.click()

    time.sleep(5)  # Wait for the login process to complete

    # Check if login was successful by finding an element only present when logged in
    if driver.find_element(By.CLASS_NAME, 'avatar-icon'):
        print(f"[SUCCESS] Logged in as {account['username']}")
    else:
        print(f"[ERROR] Failed to log in as {account['username']}")

# --- FUNCTION TO JOIN THE GAME --- #
def join_game(driver):
    driver.get(PROFILE_URL)
    time.sleep(5)  # Allow time for profile page to load

    # Wait for the "Join" button and click it
    join_button = driver.find_element(By.XPATH, '//button[@data-testid="join-button"]')
    join_button.click()

    time.sleep(5)  # Wait for the game to start loading
    print("[INFO] Joined the game successfully.")

# --- FUNCTION TO KEEP SESSION ALIVE --- #
def keep_session_alive(driver):
    while True:
        time.sleep(60)  # Keep the session alive by doing nothing

# --- MAIN FUNCTION --- #
def main():
    # Set up the WebDriver (Chrome or Firefox; you need to have the driver installed on your machine)
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for account in ACCOUNTS:
        print(f"[INFO] Starting session for {account['username']}")
        roblox_login(driver, account)
        join_game(driver)
        keep_session_alive(driver)

    driver.quit()

if __name__ == "__main__":
    main()
