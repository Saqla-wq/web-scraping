from playwright.sync_api import sync_playwright

url = "https://www.youtube.com/@MrBeast"

def scrape_youtube_channal(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("#channel-name")

        name = page.locator("yt-formatted-string#text").first.inner_text()

        subscribers = page.locator("#subscriber-count").inner_text()

        page.click("tp-yt-paper-tab:has-text('Videos')")
        videos_count = page.locator("ytd-grid-video-renderer").count()

        page.click("tp-yt-paper-tab:has-text('About')")
        description = page.locator("#description-container").inner_text()

        browser.close()

        return{
            "Channal Name" : name,
            "Subscribers" : subscribers,
            "Total Videos" : videos_count,
            "Description" : description 
        }
    
data = scrape_youtube_channal(url)
print(data)    

