import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process

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

LOGIN_URL = "https://www.roblox.com/login"
PROFILE_URL = "https://www.roblox.com/users/1759864847/profile"


def create_driver():
    """Create a headless Chrome driver."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def login_and_join(account):
    """Login to Roblox account and join Iz9vs2k."""
    driver = create_driver()
    try:
        driver.get(LOGIN_URL)
        print(f"[INFO] Logging in with account: {account['username']}")

        # Input username
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(account['username'])

        # Input password
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(account['password'])
        
        # Click login button
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        time.sleep(5)  # Wait for login to complete

        # Navigate to profile and click join
        driver.get(PROFILE_URL)
        time.sleep(5)

        join_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Join')]"))
        )
        join_button.click()
        print(f"[SUCCESS] {account['username']} successfully joined the server.")

        while True:
            time.sleep(300)  # Keep AFK indefinitely

    except Exception as e:
        print(f"[ERROR] {account['username']} failed: {e}")
    
    finally:
        driver.quit()


def main():
    processes = []
    for account in ACCOUNTS:
        process = Process(target=login_and_join, args=(account,))
        process.start()
        processes.append(process)
        time.sleep(2)  # Slight delay between logins

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
