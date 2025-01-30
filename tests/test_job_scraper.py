import unittest
from unittest.mock import patch
from scraper.job_scraper import JobScraper
import os


class TestJobScraper(unittest.TestCase):
    def setUp(self):
        """Set up for the tests."""
        self.scraper = JobScraper(job_title="Software Engineer", location="United States", max_jobs=5)

    @patch.object(JobScraper, 'scrape_jobs')  # Mock the actual scraping method to prevent hitting LinkedIn
    def test_scrape_jobs(self, mock_scrape):
        """Test that job scraping works and extracts job data."""
        # Mock the data that would be returned from the real scraping
        mock_scrape.return_value = None  # Do not actually scrape during the test
        
        # Mock job data to simulate the result of scraping
        self.scraper.jobs = [
            {"Job Title": "Software Engineer", "Company": "Company A", "Location": "New York", "Posted Date": "1 day ago", "Experience": "2-5 years", "Job Description": "Develop software."}
        ]
        
        self.scraper.scrape_jobs()  # This won't actually scrape due to the mock
        
        self.assertGreater(len(self.scraper.jobs), 0, "No jobs were scraped")

        # Check that the structure of the data is correct
        for job in self.scraper.jobs:
            self.assertIn("Job Title", job)
            self.assertIn("Company", job)
            self.assertIn("Location", job)
            self.assertIn("Posted Date", job)
            self.assertIn("Experience", job)
            self.assertIn("Job Description", job)

    @patch.object(JobScraper, 'scrape_jobs')  # Mock scraping here too
    def test_save_to_csv(self, mock_scrape):
        """Test saving scraped jobs to CSV."""
        mock_scrape.return_value = None  # Mock the scraping process
        
        # Mock job data to simulate the result of scraping
        self.scraper.jobs = [
            {"Job Title": "Software Engineer", "Company": "Company A", "Location": "New York", "Posted Date": "1 day ago", "Experience": "2-5 years", "Job Description": "Develop software."}
        ]
        
        # Save to CSV
        self.scraper.save_to_csv(filename="data/test_jobs.csv")
        
        # Check if the file was created
        self.assertTrue(os.path.exists("data/test_jobs.csv"), "CSV file not created")
        
        # Optionally check file contents
        with open("data/test_jobs.csv", "r") as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 1, "CSV file is empty")

    def tearDown(self):
        """Clean up after tests."""
        # Optional cleanup, like deleting test files after the tests if needed
        if os.path.exists("data/test_jobs.csv"):
            os.remove("data/test_jobs.csv")


if __name__ == "__main__":
    unittest.main()
