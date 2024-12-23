import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process

# List of 11 accounts with usernames and passwords
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

# Profile URL for Iz9vs2k
PROFILE_URL = "https://www.roblox.com/users/1759864847/profile"

# Function to create and return a new browser driver instance
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Use the latest version of ChromeDriver automatically
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

# Function to log in, join the game and set AFK
def login_and_join_afk(account):
    driver = create_driver()
    try:
        # Open the Roblox login page
        driver.get("https://www.roblox.com/login")

        # Find the username and password fields and enter credentials
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys(account["username"])
        password_input.send_keys(account["password"])
        login_button.click()

        # Wait for login to complete (adjust time as needed)
        time.sleep(5)

        # Go to Iz9vs2k's profile page
        driver.get(PROFILE_URL)

        # Find and click the "Join" button to join Iz9vs2k's server
        join_button = driver.find_element(By.XPATH, "//button[@aria-label='Join game']")
        join_button.click()

        # Wait for the game to load and start AFK mode
        time.sleep(10)  # Adjust time as needed

        # AFK logic (simulating no actions)
        while True:
            time.sleep(100)  # Keep the account idle

    except Exception as e:
        print(f"Error for {account['username']}: {e}")
    finally:
        driver.quit()

# Main function to manage all accounts and run them concurrently
def main():
    processes = []
    for account in ACCOUNTS:
        p = Process(target=login_and_join_afk, args=(account,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

# Execute the script
if __name__ == "__main__":
    main()
