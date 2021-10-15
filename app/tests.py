from django.test import TestCase
from app import models
# Create your tests here.
class TestJob(TestCase):
    def test_can_create_job(self):
        jobs = models.create_job(
            "Core Logic Jr Developer", 
            "Your job is to help with mortgages", 
            "Core Logic",
            "Handles Mortgages", 
            "1 year python experience", 
            "Batesville",
            10000,
            15000,
        )
        self.assertEqual(jobs.role_name, "Core Logic Jr Developer")
        self.assertEqual(jobs.role_desc, "Your job is to help with mortgages")
        self.assertEqual(jobs.company_name, "Core Logic")
        self.assertEqual(jobs.company_desc, "Handles Mortgages")
        self.assertEqual(jobs.role_req, "1 year python experience")
        self.assertEqual(jobs.location, "Batesville")
        self.assertEqual(jobs.minumum_salary, 10,000)
        self.assertEqual(jobs.miximum_salary, 15,000)
         
            # "Role": "Core Logic Jr Developer", 
            # "Description":"Your job is to help with mortgages", 
            # "Company": "Core Logic",
            # "What we do": "Handles Mortgages", 
            # "Requirements": "1 year python experience", 
            # "Location": "Batesville",
            # "Minimum Salary": 10,000,
            # "Maximum Salary": 15,000,

    def test_can_view_all_jobs(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        jobs = models.read_all_jobs()
        self.assertEqual(len(jobs), len(job_data))
        job_data = sorted(_data, key=lambda c: c["Role"])
        jobs = sorted(jobs, key=lambda c: c.role_name)
        for data, jobs in zip(job_data, jobs):
            self.assertEqual(data["Role"], jobs.role_name)
            self.assertEqual(data["Description"], jobs.role_desc)
            self.assertEqual(data["Company"], jobs.company_name)
            self.assertEqual(data["What we do"], jobs.company_desc)
            self.assertEqual(data["Requirements"], jobs.role_req)
            self.assertEqual(data["Location"], jobs.location)
            self.assertEqual(data["Minimum Salary"], jobs.minimum_salary)
            self.assertEqual(data["Maximum Salary"], jobs.maximum_salary)
    

    def test_jobs_in_location(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        job = models.read_by_loc("Batesville")
        self.assertEqual(job.location, "Batesville")


    def test_jobs_in_role(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        job = models.read_by_role_name("Head Cook")
        self.assertEqual(job.role_name, "Head Cook")
    

    def test_jobs_in_location(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        job = models.read_by_loc("Batesville")
        self.assertEqual(job.location, "Batesville")


    def test_jobs_in_role(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        self.assertEqual(len(job.find_min_salary(1000,5000)),1)
    

    def test_jobs_in_location(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        job = models.read_by_loc("Batesville")
        self.assertEqual(job.location, "Batesville")


    def test_update_location(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        models.update(1, "Water Valley")
        self.assertEqual(
            models.read_by_loc("Batesville").location, "Water Valley"
        )
    
        def test_jobs_in_location(self):
            jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        job = models.read_by_loc("Batesville")
        self.assertEqual(job.location, "Batesville")


def test_delete(self):
        jobs_data = [
            {            
             "Role": "Core Logic Jr Developer", 
             "Description":"Your job is to help with mortgages", 
             "Company": "Core Logic",
             "What we do": "Handles Mortgages", 
             "Requirements": "1 year python experience", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
            {
             "Role": "Head Cook", 
             "Description":"Your job is to help with the kitchen", 
             "Company": "Sprint-Mart",
             "What we do": "Cook Food", 
             "Requirements": "1 year cooking experience", 
             "Location": "Batesville",
             "Minimum Salary": 1000,
             "Maximum Salary": 5000,
            },
            {
             "Role": "C-Spire Jr Developer", 
             "Description":"Your job is to help with styling of the C-Spire website", 
             "Company": "C-Spire",
             "What we do": "Handle Web-Design", 
             "Requirements": "1 year HTML, CSS, and Javascript", 
             "Location": "Batesville",
             "Minimum Salary": 10000,
             "Maximum Salary": 15000,
            },
        ]
        for job_data in jobs_data:
            models.create_job(
                job_data["Role"],
                job_data["Description"],
                job_data["Company"],
                job_data["What we do"],
                job_data["Requirements"],
                job_data["Location"],
                job_data["Minimun Salary"],
                job_data["Maximum Salary"],

            )
        models.delete(2)
        self.assertEqual(len(models.read_all_jobs()), 2)
