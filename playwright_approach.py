import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the initial page
        await page.goto('https://instagram.com/')
        
        await asyncio.sleep(5)

        # Fill in username and password fields
        await page.fill("input[name='username']", "ithinktheytoldthewarden")
        await page.fill("input[name='password']", "lndlndlnd")

        await asyncio.sleep(5)
        
        # Click the submit button
        await page.click("button[type='submit']")

        # Wait for the page to load (adjust as needed)
        await asyncio.sleep(5)

        # Handle 'Not Now' buttons
        for _ in range(2):
            try:
                # Wait for 'Not Now' button to be clickable
                not_now_button = await page.wait_for_selector("//button[@class='aOOlW   HoLwm ']", state='visible', timeout=5000)
                await not_now_button.click()
            except Exception as e:
                print(f"Could not find 'Not Now' button: {e}")

            await asyncio.sleep(5)

        await asyncio.sleep(100)

        await browser.close()

asyncio.run(main())
