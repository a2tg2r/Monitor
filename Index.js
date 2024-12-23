const puppeteer = require('puppeteer');

// --- CONFIGURATION --- //
const ACCOUNTS = [
    { username: "KiwiSubZeroPTG", password: "14670qeyip" },
    { username: "Farmerinmm29", password: "1234567890qeyip" },
    { username: "Farmermm2299", password: "1234567890qeyip" },
    { username: "M2farm8", password: "101113LK" },
    { username: "10farm18", password: "101113LK" },
    { username: "Mm2craxyfarm0", password: "1234567890qeyip" },
    { username: "Mm2craxyfarm01", password: "1234567890qeyip" },
    { username: "Mm2craxyfarm02", password: "1234567890qeyip" },
    { username: "Mm2craxyfarm03", password: "1234567890qeyip" },
    { username: "Mm2craxyfarm5", password: "1234567890qeyip" },
    { username: "Mm2craxyfarm11", password: "1234567890qeyip" }
];

const PROFILE_URL = "https://www.roblox.com/users/1759864847/profile";  // Iz9vs2k's Profile URL

// --- FUNCTION TO LOG IN TO ROBLOX --- //
async function robloxLogin(page, account) {
    await page.goto('https://www.roblox.com/login');

    await page.type('input[name="username"]', account.username, { delay: 100 });
    await page.type('input[name="password"]', account.password, { delay: 100 });

    // Click the correct "Log In" button
    await page.click('button[data-testid="login-button"]');  // Ensure we're selecting the correct login button

    await page.waitForNavigation({ waitUntil: 'networkidle0' });

    // Check if logged in successfully
    const loggedIn = await page.evaluate(() => {
        return document.querySelector('.avatar-icon') !== null;
    });

    if (loggedIn) {
        console.log(`[SUCCESS] Logged in as ${account.username}`);
    } else {
        console.error(`[ERROR] Failed to log in as ${account.username}`);
    }
}

// --- FUNCTION TO JOIN THE GAME --- //
async function joinGame(page) {
    await page.goto(PROFILE_URL);

    // Wait for the page to load and check if the "Join" button is available
    await page.waitForSelector('button[data-testid="join-button"]', { timeout: 5000 });

    // Click the "Join" button
    await page.click('button[data-testid="join-button"]');

    // Wait for the game to start loading
    await page.waitForNavigation({ waitUntil: 'networkidle0' });

    console.log(`[INFO] Joined the game successfully.`);
}

// --- FUNCTION TO KEEP SESSION ALIVE --- //
async function keepSessionAlive(page) {
    setInterval(async () => {
        await page.reload();
    }, 60000);  // Reload every 60 seconds to keep the session alive
}

// --- MAIN FUNCTION --- //
async function main() {
    const browser = await puppeteer.launch({ headless: false, defaultViewport: null });
    const page = await browser.newPage();

    for (const account of ACCOUNTS) {
        console.log(`[INFO] Starting session for ${account.username}`);

        await robloxLogin(page, account);
        await joinGame(page);
        keepSessionAlive(page);
    }

    // Keep browser open
    //await browser.close(); // Uncomment this if you want to close the browser after the process is done
}

main().catch(err => console.error(`[ERROR] An error occurred: ${err}`));
