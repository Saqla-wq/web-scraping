
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

video_url = "https://www.youtube.com/@MrBeast/videos"

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto(video_url, wait_until="domcontentloaded")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(60000)
    html = page.content()

    with open("video_page.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")
     
    content_list = page.locator("#content").count()
    number = 1


    with open("youtube_videos.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Views", "Upload Date"])

        for i in range(content_list):
            content_element = page.locator("#content").nth(i)
            video_links = content_element.locator("yt-formatted-string#video-title").all_text_contents()
            views = content_element.locator("#metadata-line span").all_text_contents()
            upload_date = content_element.locator("#metadata-line span").nth(1).all_text_contents()

            for video_link in video_links:
                title = video_link.strip()
                view_text = views[0].strip() if len(views) > 0 else "N/A"
                date_text = upload_date[0].strip() if len(upload_date) > 0 else "N/A"

                print(f"{number}. {title} | {view_text} | {date_text}")

                writer.writerow([title, view_text, date_text])

                number += 1

    print("Total videos Found :", content_list)
    browser.close()



