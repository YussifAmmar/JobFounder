import json
import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_jobs(DesiredJob = "Mahchine Learning" ,location= "Egypt", cookies_file="cookies.json", csv_filename="Jobs.csv"):
    
    DesiredJob = DesiredJob.split(" ")
    JobTitle = "%20".join(DesiredJob)
    service = Service()
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.linkedin.com")
    time.sleep(5)

    with open(cookies_file, "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        if 'sameSite' in cookie:
            cookie.pop('sameSite')
        driver.add_cookie(cookie)

    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)
    print("Logged in successfully!")

    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={JobTitle}&location={location}")

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container__link"))
    )

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container__link")
    job_list = []

    for job in jobs[:10]: 
        title = job.text.strip()
        link = job.get_attribute("href")

        try:
            desc_element = job.find_element(By.ID, "job-details")
            desc = desc_element.text.strip()
        except:
            desc = "Description not available."

        if title and link:
            job_list.append([title, link, desc])

   
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Job Link", "Job Description"])
        writer.writerows(job_list)

    print(f"Saved {len(job_list)} jobs to {csv_filename}")

    if job_list:
        #message = "New ML Jobs in Egypt:\n\n" + "\n\n".join(
            [f"{title}\n{link}" for title, link, _ in job_list]
        )
    else:
        message = "No jobs found!"

    #send_telegram(bot_token, chat_id, message)

    driver.quit()

