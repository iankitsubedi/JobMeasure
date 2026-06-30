from playwright.sync_api import Page
from playwright_stealth import Stealth
import csv
import os

# defining the required playwright function
def test_naukri(page: Page):
    # Stealth required to work with the website
    Stealth().apply_stealth_sync(page) 

    # Working with the head mode of the playwright 
    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    file_path = r"C:\Users\bimal\OneDrive\Documents\Thing\The project\JobMeasure\src\scrapper\raw_data\naukri_raw.csv"
    file_exists = os.path.exists(file_path)

    # Extracting the data from the website
    with open(file_path,"a",newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Job_title","Company_name","Required_time_experience","Salary","Job_location","Skill"])

        for offset in range(1,501):
            # try except condition if page gets blocked 
            try:
                page.goto(f"https://www.naukri.com/jobs-in-india-{offset}?functionAreaIdGid=3&functionAreaIdGid=4&functionAreaIdGid=5&functionAreaIdGid=8&clusters=functionalAreaGid", timeout=60000)
            except:
                print(f"Page {offset} blocked,skipping it.")
                page.wait_for_timeout(10000)
                continue

            page.wait_for_timeout(5000)
            cards = page.locator("div.srp-jobtuple-wrapper").all()

            if len(cards) == 0:
                break

            for i in cards:
                Job = i.locator("a.title").text_content(timeout=4000).strip()
                company_name = i.locator("a.comp-name").text_content(timeout=4000).strip()
                
                try:
                    experience = i.locator("span.expwdth").text_content(timeout=2000).strip()
                except:
                    experience = "Not Provided"

                try:
                    job_location = i.locator("span.locWdth").text_content(timeout=500).strip()
                except:
                    job_location = "Not Provided"

                skills = i.locator("ul.tags-gt li").all()
                skills_list = [s.text_content() for s in skills]

                try:
                    salary = i.locator("span.sal-wrap").locator("span").nth(1).text_content(timeout=500).strip()
                except:
                    salary = "Not Provided"

                print(Job, "=>", company_name, "=>", experience, "=>", salary, "=>", job_location, "=>", skills_list)
                print("\n")
                writer.writerow([Job,company_name,experience,salary,job_location,", ".join(skills_list)])

            
  