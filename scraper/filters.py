class JobFilters:
    def __init__(self, experience=None, location=None, job_title=None):
        self.experience = experience
        self.location = location
        self.job_title = job_title

    def apply_filters(self, job_listings):
        """Apply all active filters to the job listings."""
        filtered_jobs = job_listings

        if self.job_title:
            filtered_jobs = self.filter_by_job_title(filtered_jobs)
        if self.location:
            filtered_jobs = self.filter_by_location(filtered_jobs)
        if self.experience:
            filtered_jobs = self.filter_by_experience(filtered_jobs)

        return filtered_jobs

    def filter_by_job_title(self, job_listings):
        """Filter jobs by job title."""
        return [job for job in job_listings if self.job_title.lower() in job["Job Title"].lower()]

    def filter_by_location(self, job_listings):
        """Filter jobs by location."""
        return [job for job in job_listings if self.location.lower() in job["Location"].lower()]

    def filter_by_experience(self, job_listings):
        """Filter jobs by experience requirement."""
        return [job for job in job_listings if self.experience.lower() in job["Experience"].lower()]

