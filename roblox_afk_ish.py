import requests
import logging

# --- CONFIGURATION --- #
ACCOUNTS = [
    {"username": "KiwiSubZeroPTG", "password": "14670qeyip"},
    {"username": "Farmerinmm29", "password": "1234567890qeyip"},
    {"username": "Farmermm2299", "password": "1234567890qeyip"},
    {"username": "Farmerincrazy", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm", "password": "123456qeyip"},
    {"username": "Mm2craxyfarm0", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm01", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm02", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm03", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm5", "password": "1234567890qeyip"},
    {"username": "Mm2craxyfarm11", "password": "1234567890qeyip"}
]

LOGIN_URL = "https://www.roblox.com/login"
FRIEND_PROFILE_URL = "https://www.roblox.com/users/1759864847/profile"
GAME_URL = "https://www.roblox.com/games/142823291/Murder-Mystery-2"

# --- LOGGING SETUP --- #
logging.basicConfig(
    filename='afk_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("AFK script started")


# --- FUNCTION TO LOG IN TO ROBLOX --- #
def roblox_login(account):
    session = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": account['username'],
        "password": account['password']
    }

    try:
        response = session.post(LOGIN_URL, data=payload, headers=headers)
        if response.status_code == 200 and '.ROBLOSECURITY' in session.cookies:
            logging.info(f"[SUCCESS] Logged in as {account['username']}")
            return session
        else:
            logging.error(f"[ERROR] Failed to log in as {account['username']}: {response.text}")
            return None
    except Exception as e:
        logging.error(f"[ERROR] Exception during login for {account['username']}: {e}")
        return None


# --- FUNCTION TO VISIT FRIEND'S PROFILE PAGE --- #
def visit_friend_profile(session, account):
    try:
        response = session.get(FRIEND_PROFILE_URL)
        if response.status_code == 200:
            logging.info(f"[SUCCESS] {account['username']} accessed friend's profile page.")
            return True
        else:
            logging.error(f"[ERROR] {account['username']} failed to access profile page: {response.text}")
            return False
    except Exception as e:
        logging.error(f"[ERROR] Exception accessing profile for {account['username']}: {e}")
        return False


# --- FUNCTION TO OPEN GAME URL --- #
def open_game_url(session, account):
    try:
        response = session.get(GAME_URL)
        if response.status_code == 200:
            logging.info(f"[SUCCESS] {account['username']} navigated to the game page.")
            return True
        else:
            logging.error(f"[ERROR] {account['username']} failed to access game page: {response.text}")
            return False
    except Exception as e:
        logging.error(f"[ERROR] Exception opening game for {account['username']}: {e}")
        return False


# --- FUNCTION TO KEEP SESSION ALIVE --- #
def keep_session_alive(account):
    logging.info(f"[INFO] {account['username']} is now AFK indefinitely.")
    while True:
        try:
            pass  # Keeps the session alive indefinitely
        except KeyboardInterrupt:
            logging.info(f"[INFO] Script manually stopped for {account['username']}.")
            break
        except Exception as e:
            logging.error(f"[ERROR] Session error for {account['username']}: {e}")
            break


# --- MAIN FUNCTION --- #
def main():
    for account in ACCOUNTS:
        logging.info(f"[INFO] Starting session for {account['username']}")
        session = roblox_login(account)
        
        if session:
            if visit_friend_profile(session, account):
                if open_game_url(session, account):
                    keep_session_alive(account)
                else:
                    logging.error(f"[ERROR] Could not open game for {account['username']}")
            else:
                logging.error(f"[ERROR] Could not visit profile for {account['username']}")
        else:
            logging.error(f"[ERROR] Could not log in for {account['username']}")

if __name__ == "__main__":
    main()
