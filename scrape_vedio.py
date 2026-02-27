from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

video_url = "https://youtu.be/E4wU8y7r1Uc?si=xO7K_hNEsq6T4-bo"

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto(video_url)
    page.wait_for_load_state("networkidle")
    html = page.content()
    print(html)
    
    with open("video_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("title")
    print("Video Title:", title.text)
       
    views = page.locator("#info span.view-count").first.inner_text()
    print("Views:", views)

    channel_name = page.locator("#channel-name a").text_content()
    print("Channel Name:", channel_name)
    
    upload_date = page.locator("#info-strings yt-formatted-string").text_content()
    print("Upload Date:", upload_date)

    browser.close()

