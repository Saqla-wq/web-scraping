



from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() 
    page.goto("https://crexed.com/about")
    page.wait_for_load_state("networkidle")
    context = browser.new_context

    html_content = page.content()
    print(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("a")
    
    for link in links:
        print(link.get("href"))
    
    browser.close() 



 
# for page vedio load 
# page.goto("https://example.com/video-page")
# page.wait_for_timeout(5000)  
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