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

# URLs to interact with
LOGIN_URL = "https://www.roblox.com/login"
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
    session = requests.Session()  # Maintain session for cookies
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    payload = {
        "username": account["username"],
        "password": account["password"],
        "remember": "true"  # Option to keep the session alive
    }

    try:
        # Send POST request with username/password
        response = session.post(LOGIN_URL, data=payload, headers=headers)
        if response.status_code == 200 and '.ROBLOSECURITY' in session.cookies:
            logging.info(f"[SUCCESS] Logged in as {account['username']}")
            return session  # Return session for future requests
        else:
            logging.error(f"[ERROR] Failed to log in as {account['username']}")
            return None
    except Exception as e:
        logging.error(f"[ERROR] Exception during login for {account['username']}: {e}")
        return None

# --- FUNCTION TO OPEN THE GAME URL --- #
def open_game_url(session, account, server_id=None):
    try:
        # If we have a specific server_id, join the same server
        if server_id:
            game_url = f"{GAME_URL}?serverPlaceId={server_id}"
        else:
            game_url = GAME_URL
        
        response = session.get(game_url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            logging.info(f"[SUCCESS] {account['username']} navigated to the game page.")
            return True
        else:
            logging.error(f"[ERROR] {account['username']} failed to access game page.")
            return False
    except Exception as e:
        logging.error(f"[ERROR] Exception opening game for {account['username']}: {e}")
        return False

# --- FUNCTION TO KEEP SESSION ALIVE --- #
def keep_session_alive(account):
    logging.info(f"[INFO] {account['username']} is now AFK indefinitely.")
    while True:
        try:
            pass  # Infinite loop to keep the session alive
        except KeyboardInterrupt:
            logging.info(f"[INFO] Script manually stopped for {account['username']}.")
            break
        except Exception as e:
            logging.error(f"[ERROR] Session error for {account['username']}: {e}")
            break

# --- MAIN FUNCTION --- #
def main():
    server_id = None  # Variable to store the server ID for the game
    
    for index, account in enumerate(ACCOUNTS):
        logging.info(f"[INFO] Starting session for {account['username']}")
        session = roblox_login(account)
        
        if session:
            # If this is the first account, get the server ID
            if index == 0:
                # First account joins the game and gets the server_id from the URL
                if open_game_url(session, account):
                    logging.info(f"[INFO] {account['username']} joined the game, fetching server ID.")
                    # In a real scenario, you'd need to extract the server ID from the page response or URL
                    # For now, we just use the server ID as a placeholder or static URL
                    server_id = "YOUR_SERVER_ID"  # Replace with the actual server ID dynamically
                else:
                    logging.error(f"[ERROR] {account['username']} failed to join the game.")
                    continue
            
            # After the first account joins, all others join the same server
            if server_id and open_game_url(session, account, server_id):
                logging.info(f"[SUCCESS] {account['username']} joined the same server.")
                keep_session_alive(account)
            else:
                logging.error(f"[ERROR] {account['username']} could not join the same server.")

        else:
            logging.error(f"[ERROR] Could not log in for {account['username']}")

if __name__ == "__main__":
    main()
