from django.db import models

# Create your models here.
class Job(models.Model):
    role_name: models.TextField()
    role_desc: models.TextField()
    company_name: models.TextField()
    company_desc: models.TextField()
    role_req: models.TextField()
    location: models.TextField()
    minimum_salary: models.IntegerField()
    maximum_salary: models.IntegerField()

def create_job(rolename, roledes, comname, comdesc, rolreq, location, min_sal, max_sal):
    jobs = Job(role_name=rolename, role_desc=roledes, company_name=comname, company_desc=comdesc, role_req=rolreq, location=location, minimum_salary=min_sal, maximum_salary=max_sal)
    jobs.save()
    return jobs

def read_all_jobs():
    return Job.objects.all()

def read_by_loc(location):
    try:
        return Job.objects.get(location=location)
    except:
        return None

def read_by_role_name(rolename):
    try:
        return Job.objects.get(role_name=rolename)
    except:
        return None

def find_min_salary(min_sal, max_sal):
    return Job.objects.filter(minimum_salary=min_sal, maximum_salary=max_sal)

def update(id, new_location):
    job=Job.objects.get(id=id)
    job.location=new_location
    job.save()

def delete(id):
    job = Job.objects.get(id=id)
    job.delete()