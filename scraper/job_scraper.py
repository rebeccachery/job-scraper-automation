from playwright.sync_api import sync_playwright
import pandas as pd
import time

class JobScraper:
    def __init__(self, job_title, location, max_jobs=10):
        self.job_title = job_title
        self.location = location
        self.max_jobs = max_jobs
        self.jobs = []

    def scrape_jobs(self):
        """Scrapes job postings from LinkedIn with improved efficiency."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # LinkedIn Jobs Search URL
            search_url = f"https://www.linkedin.com/jobs/search/?keywords={self.job_title}&location={self.location}"
            page.goto(search_url, timeout=60000)
            time.sleep(5)

            # Scroll to load more job listings
            self.scroll_to_load_jobs(page)

            job_listings = page.locator(".jobs-search-results__list-item").all()

            # Scrape the specified number of jobs
            for job in job_listings[:self.max_jobs]:
                self.extract_job_details(job, page)

            browser.close()

    def scroll_to_load_jobs(self, page, scroll_count=5):
        """Scrolls the page to load more job listings."""
        for _ in range(scroll_count):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)  # Allow more jobs to load

    def extract_job_details(self, job, page):
        """Extracts detailed information from a single job posting."""
        job.click()
        time.sleep(3)  # Allow job details to load

        try:
            job_title = page.locator(".t-24").text_content().strip()
            company = page.locator(".job-search-card__company-name").text_content().strip()
            location = page.locator(".jobs-unified-top-card__bullet").nth(0).text_content().strip()
            posted_date = page.locator(".posted-time-ago__text").text_content().strip()
            job_desc = page.locator(".jobs-description__content").text_content().strip()

            # Extract experience details (if available)
            experience = self.extract_experience(page)

            self.jobs.append({
                "Job Title": job_title,
                "Company": company,
                "Location": location,
                "Posted Date": posted_date,
                "Experience": experience,
                "Job Description": job_desc
            })

        except Exception as e:
            print(f"Error extracting job: {e}")

    def extract_experience(self, page):
        """Extracts experience requirements, if available."""
        try:
            experience = page.locator('.job-criteria__list li:nth-child(1)').text_content().strip()
        except:
            experience = "Not listed"
        return experience

    def save_to_csv(self, filename="data/linkedin_jobs.csv"):
        """Saves job postings to a CSV file."""
        df = pd.DataFrame(self.jobs)
        df.to_csv(filename, index=False)
        print(f"Saved {len(self.jobs)} jobs to {filename}")

if __name__ == "__main__":
    scraper = JobScraper(job_title="Software Engineer", location="United States", max_jobs=10)
    scraper.scrape_jobs()
    scraper.save_to_csv()
