from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://crexed.com/")
    page.screenshot(path="page.png") # for page 
    browser.close()


# For Full Page screen shoot we can add this :  path = "full_page.png", full_page=True

# For Specific Element: 
    # element = page.locator("h1")
    # element.screenshot(path="heading.png")   

