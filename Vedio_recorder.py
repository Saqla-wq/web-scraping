from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",  # vedio wala folder jahan vedio save hogi 
        record_video_size={"width": 1280, "height": 720}
    )
    
    page = context.new_page()
    
    page.goto("https://crexed.com/")
    
    # page.click("text=More information")

    context.close()   
    browser.close()