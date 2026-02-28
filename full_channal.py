from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

video_url = "https://www.youtube.com/@MrBeast/videos"

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto(video_url)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(60000)
    html = page.content()

    with open("video_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
     
    
      
    content_list = page.locator("#content").count()
    number = 1

    for i in range(content_list):
        content_element = page.locator("#content").nth(i)
        video_links = content_element.locator("yt-formatted-string#video-title").all_text_contents()
        for video_link in video_links:
                print(f"{number}. {video_link.strip()}")  
                number += 1         


    print("Total videos Found :", content_list)

    

    browser.close()



