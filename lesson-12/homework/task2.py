import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

DB_NAME = "jobs.db"
URL = "https://realpython.github.io/fake-jobs"

# Create SQLite table
def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                apply_link TEXT,
                UNIQUE(job_title, company, location)
            )
        ''')
        conn.commit()

# Scrape job listings
def scrape_jobs():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")
    
    jobs = []
    for job_element in job_elements:
        title = job_element.find("h2", class_="title")
        company = job_element.find("h3", class_="company")
        location = job_element.find("p", class_="location")
        description = job_element.find("div", class_="content")
        apply_link = job_element.find("a", text="Apply")
        
        if title and company and location and description and apply_link:
            jobs.append((
                title.text.strip(),
                company.text.strip(),
                location.text.strip(),
                description.text.strip(),
                apply_link["href"].strip()
            ))
    
    return jobs

# Insert new jobs and update existing ones
def save_jobs(jobs):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for job in jobs:
            cursor.execute('''
                INSERT INTO jobs (job_title, company, location, description, apply_link) 
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(job_title, company, location) 
                DO UPDATE SET description=excluded.description, apply_link=excluded.apply_link
            ''', job)
        conn.commit()

# Filter jobs by location or company
def filter_jobs(location=None, company=None):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query = "SELECT job_title, company, location, description, apply_link FROM jobs WHERE 1=1"
        params = []
        if location:
            query += " AND location = ?"
            params.append(location)
        if company:
            query += " AND company = ?"
            params.append(company)
        cursor.execute(query, params)
        return cursor.fetchall()

# Export jobs to CSV
def export_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    create_table()
    jobs = scrape_jobs()
    if jobs:
        save_jobs(jobs)
        print("Job listings updated successfully.")
    else:
        print("No new job listings found.")
