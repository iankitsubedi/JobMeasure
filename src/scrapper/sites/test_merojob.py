from playwright.sync_api import Page
import csv

# defining the required playwright function
def test_merojob(page : Page):

    # creating a new csv file for the data
    with open(r"C:\Users\bimal\OneDrive\Documents\Thing\The project\JobMeasure\src\scrapper\raw_data\merojob_raw.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job_title","Company_name","Job_location","Salary","Job_time","Skills"])

        # extracting the data from merojob
        for offset in range(1,50):
            page.goto(f"https://merojob.com/category/it-telecommunication?limit=6&offset={offset}",wait_until = "domcontentloaded" ,timeout=60000)
            page.wait_for_timeout(10000)

            cards = page.locator("div.my-4.break-words").all()
            if len(cards) == 0:
                break
            
            for i in cards:
                titles = i.locator("span.text-blue-900").text_content()
                company_name = i.locator("span.text-sm").text_content()
                location = i.locator("span.line-clamp-1 span").text_content()
                checkingsalary = i.locator("p.whitespace-nowrap").text_content()
                jobtime = i.locator("p.flex.items-center.gap-2").text_content()
                skills = i.locator('div[data-sentry-component="Badge"]').all() 
                skill_list = [s.text_content() for s in skills]
                writer.writerow([titles,company_name,location,checkingsalary,jobtime,", ".join(skill_list)])
                # print(titles, "->", company_name, "->", location,"->",checkingsalary,"->",jobtime,"->",skill_list)
                # print("\n")

            

        