from scraper.job_scraper import JobScraper
from filters import JobFilters
import pandas as pd

def main():
    # Define search parameters
    job_title = "Software Engineer"
    location = "United States"
    max_jobs = 10

    # Initialize the scraper
    scraper = JobScraper(job_title=job_title, location=location, max_jobs=max_jobs)
    scraper.scrape_jobs()

    # Apply filters if needed (e.g., filter by experience)
    filters = JobFilters(experience="5+ years", location="Remote")  # Example filters
    filtered_jobs = filters.apply_filters(scraper.jobs)

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(filtered_jobs)
    df.to_csv("data/filtered_jobs.csv", index=False)
    print(f"Saved {len(filtered_jobs)} filtered jobs to data/filtered_jobs.csv")

if __name__ == "__main__":
    main()
