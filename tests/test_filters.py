import unittest
from scraper.filters import JobFilters

class TestJobFilters(unittest.TestCase):
    def setUp(self):
        """Set up for the tests."""
        # Sample data of job listings to be used in the tests
        self.job_listings = [
            {"Job Title": "Software Engineer", "Location": "New York", "Experience": "2-5 years"},
            {"Job Title": "Data Scientist", "Location": "San Francisco", "Experience": "3-5 years"},
            {"Job Title": "Software Engineer", "Location": "Chicago", "Experience": "1-3 years"},
        ]

    def test_filter_by_job_title(self):
        """Test filtering by job title."""
        filters = JobFilters(job_title="Software Engineer")
        filtered_jobs = filters.apply_filters(self.job_listings)
        
        self.assertEqual(len(filtered_jobs), 2)
        self.assertTrue(all("Software Engineer" in job["Job Title"] for job in filtered_jobs))

    def test_filter_by_location(self):
        """Test filtering by location."""
        filters = JobFilters(location="San Francisco")
        filtered_jobs = filters.apply_filters(self.job_listings)
        
        self.assertEqual(len(filtered_jobs), 1)
        self.assertTrue(all("San Francisco" in job["Location"] for job in filtered_jobs))

    def test_filter_by_experience(self):
        """Test filtering by experience."""
        filters = JobFilters(experience="3-5 years")
        filtered_jobs = filters.apply_filters(self.job_listings)
        
        self.assertEqual(len(filtered_jobs), 2)
        self.assertTrue(all("3-5 years" in job["Experience"] for job in filtered_jobs))

    def test_apply_multiple_filters(self):
        """Test applying multiple filters."""
        filters = JobFilters(job_title="Software Engineer", location="Chicago")
        filtered_jobs = filters.apply_filters(self.job_listings)
        
        self.assertEqual(len(filtered_jobs), 1)
        self.assertTrue(all("Software Engineer" in job["Job Title"] and "Chicago" in job["Location"] for job in filtered_jobs))

if __name__ == "__main__":
    unittest.main()
