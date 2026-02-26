# import requests
# from bs4 import BeautifulSoup


# url = "https://crexed.com/about"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# # first_p = soup.find("p")
# # print(first_p.text.strip())

# all_p = soup.find_all("p") 
# for i, p in enumerate(all_p, start=1):
#     print(f"Paragraph {i}:", p.text.strip())

# # from urllib.request import urlopen
# # html = urlopen('http://pythonscraping.com/pages/page2.html')
# # print(html.read())

# # print(soup.prettify())







# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto ("https://www.youtube.com/@MrBeast/videos")
    



#     html = page.content()

# with open("mrbeast.html", "r", encoding="utf-8") as f:
#     html = f.read()

# soup = BeautifulSoup(html, "html.parser")

# videos = soup.find_all("ytd-rich-item-renderer")

# for video in videos:
#     title_tag = video.find("a", id="video-title")
    
#     if title_tag:
#         title = title_tag.get_text(strip=True)
#         link = "https://www.youtube.com" + title_tag["href"]
        
#         print("Title:", title)
#         print("Link:", link)
#         print("-" * 50)

#     browser.close()

# print("html saved successfully")    







# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup
# import time , requests

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto("https://crexed.com/about")
#     page.wait_for_timeout(50000)
#     response = requests.get(page.goto)

#     for _ in range(5):
#         page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         page.wait_for_timeout(30000)

#     html = page.content()

# soup = BeautifulSoup(response.text, "html.parser")

# first_p = soup.find("p")
# print(first_p.text.strip())

# browser.close()




# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# VIDEO_URL = "https://youtu.be/5OLs1GWB4OA?si=zJ9BQAwYNqr6aCHh"

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto(VIDEO_URL)
#     page.wait_for_selector("h1.title")
#     page.wait_for_load_state("networkidle")
#     html = page.content()

# soup = BeautifulSoup(html, "html.parser")


# title_tag = soup.find("h1")
# if title_tag:
#     print("Title:", title_tag.get_text(strip=True))


# channel_tag = soup.find("ytd-channel-name")
# if channel_tag:
#     print("Channel:", channel_tag.get_text(strip=True))


# description_tag = soup.find("yt-formatted-string", {"class": "content"})
# if description_tag:
#     print("Description:", description_tag.get_text(strip=True))

# view_tag = soup.find("span", {"class": "view-count"})
# if view_tag:
#     print("Views:", view_tag.get_text(strip=True))


#     browser.close()



# from playwright.sync_api import sync_playwright

# VIDEO_URL = "https://youtu.be/5OLs1GWB4OA?si=zJ9BQAwYNqr6aCHh"

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto(VIDEO_URL, timeout=60000)

#     page.wait_for_load_state("domcontentloaded")

#     page.wait_for_load_state("networkidle")

#     html = page.content()

#     print(html)  




from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() 
    page.goto("https://crexed.com/about")
    page.wait_for_load_state("networkidle")
    context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 640, "height": 480}
)
    html_content = page.content()
    print(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("a")
    
    for link in links:
        print(link.get("href"))
    
    browser.close() 



 
# for page vedio load 
# page.goto("https://example.com/video-page")
# page.wait_for_timeout(5000)  # 5 sec wait for video load
# html_content = page.content()
# print(html_content)


# https://youtu.be/XVv6mJpFOb0?si=N2Re8ZAo8qbUwm7G



# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# with sync_playwright() as p:
    
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page() 
#     page.goto("https://youtu.be/XVv6mJpFOb0?si=N2Re8ZAo8qbUwm7G")
#     page.wait_for_timeout(5000) 
#     page.screenshot(path="example.png")
#     html_content = page.content()
#     print(html_content)
#     soup = BeautifulSoup(html_content, "html.parser")
#     links = soup.find_all("a")
    
#     for link in links:
#         print(link.get("href"))
    
#     browser.close() 