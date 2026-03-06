from playwright.sync_api import sync_playwright
import csv


def scrape_crexed_projects():

    url = "https://crexed.vercel.app/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")

        # Making a csv file 
        file = open("crexed_projects.csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Languages", "Visit Site"])



        project_titles = page.locator("h2")
        count = project_titles.count()
        for i in range(count):
            title = project_titles.nth(i).inner_text().strip()
            if title in [
                "Our Amazing Projects",
                "Tech Stack",
                "Wow! This Is Amazing",
                "Ready to Elevate Your Business?",
                "The 6D Framework",
                "Ready to Get in Touch?"
            ]:
                continue
            container = project_titles.nth(i).locator("xpath=ancestor::div[1]")




            # Description scraping 
            description = ""
            desc = container.locator("p")
            if desc.count() > 0:
                description = desc.first.inner_text().strip()



            # Languages scraping 
            languages = []
            tech_items = container.locator("li").all_text_contents()
            for tech in tech_items:
                tech = tech.strip()
                if ":" in tech:
                    tech = tech.split(":")[1].strip()

                if tech and tech not in languages:
                    languages.append(tech)

            # Case study links

            visit_site = ""
            case_btn = container.locator("a:has-text('Case Study')")
            if case_btn.count() > 0:
                case_link = case_btn.first.get_attribute("href")
                if case_link:
                    page.goto(case_link)
                    page.wait_for_load_state("networkidle")
                    page.mouse.wheel(0, 8000)
                    page.wait_for_timeout(2000)
                    visit_btn = page.locator("a:has-text('Visit Site')")
                    if visit_btn.count() > 0:
                        visit_site = visit_btn.first.get_attribute("href")

                    page.go_back()
                    page.wait_for_load_state("networkidle")

            # convert languages list to string
            languages_str = ", ".join(languages)

            writer.writerow([title, description, languages_str, visit_site])

            print("\nProject")
            print("Title:", title)
            print("Description:", description)
            print("Languages:")

            for lang in languages:
                print("  -", lang)
            print("Visit Site:", visit_site)

        file.close()
        browser.close()

scrape_crexed_projects()