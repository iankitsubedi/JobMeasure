from playwright.sync_api import Page
import csv

def test_kumarijob(page : Page):
    with open(r"C:\Users\bimal\OneDrive\Documents\Thing\The project\JobMeasure\src\scrapper\raw_data\kumarijob_raw.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job_title","Company_name","Job_location","Salary","Job_time"])

        page.goto("https://www.kumarijob.com/jobs-in-nepal/it-programming-development-jobs-in-nepal",timeout=60000)
        print(page.title())
        cards = page.locator("div.job-container.bg-white.p-4").all()
        
        
        for i in cards:
            job = i.locator("h2.mb-0 a").text_content()
            company_name = i.locator("p.pe-2").text_content().strip()
            location = i.locator("span.district-text").text_content().strip()
            writer.writerow([job,company_name,location,"Negotiable","Not-provided"])
            # print(job, "->", company_name, "->", location)
      


        
