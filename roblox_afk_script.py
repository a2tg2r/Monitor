import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Define the list of accounts to be used
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

# Function to create the WebDriver
def create_driver():
    try:
        # Ensure that the webdriver manager downloads the correct version
        driver_path = ChromeDriverManager().install()

        # Setting up Chrome options for headless browsing
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Set up the service with the installed ChromeDriver
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        return driver
    except Exception as e:
        print(f"Error occurred while setting up the driver: {e}")
        return None

# Login and join AFK (example function - modify based on game)
def login_and_join_afk(account):
    driver = create_driver()
    if not driver:
        print("Could not create driver, exiting.")
        return

    try:
        driver.get("https://www.roblox.com/login")
        time.sleep(3)

        # Find and fill in the username and password fields
        driver.find_element("name", "username").send_keys(account["username"])
        driver.find_element("name", "password").send_keys(account["password"])

        driver.find_element("xpath", '//button[contains(text(),"Log In")]').click()
        time.sleep(5)

        # Navigate to game or perform AFK action here
        print(f"Logged in as {account['username']}")

        # Example action - You can adjust this based on your game
        # driver.get("URL_of_the_game")
        # time.sleep(30)  # Let the game run AFK for a while

    except Exception as e:
        print(f"Error during login/join action: {e}")
    finally:
        driver.quit()

# Main logic to loop through accounts
def main():
    for account in ACCOUNTS:
        login_and_join_afk(account)

if __name__ == "__main__":
    main()
