from playwright.sync_api import Page
import csv

# defining the required playwright function
def test_jobsnepal(page : Page):

    with open(r"C:\Users\bimal\OneDrive\Documents\Thing\The project\JobMeasure\src\scrapper\raw_data\jobsnepal_raw.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job_title","Company_name","Job_location","Salary","Job_time"])

        # extracting the data from jobsnepal
        page.goto("https://www.jobsnepal.com/category/information-technology-jobs",timeout=30000)
        cards = page.locator("div.col-md-12.mb-3").all()

        for i in cards:
            job_title = i.locator("h2.job-title a").text_content().strip()
            company_name = i.locator("p.mb-0").text_content().strip()

            # try/except used because not all jobs show location and salary
            try:
                job_location = i.locator("i.icon-location4").locator("..").locator("div").text_content(timeout=2000).strip()
            except:
                job_location = "Not Provided"
            try:
                salary = i.locator("i.icon-coin-dollar").locator("..").locator("div").text_content(timeout=2000).strip()
            except:
                salary = "Not Provided / Negotiable"
            

            writer.writerow([job_title,company_name,job_location,salary,"Not-provided"])



        