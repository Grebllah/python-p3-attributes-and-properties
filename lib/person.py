#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "name", job = "Programmer"):
        self.name = name
        self.job = job
    def get_name (self):
        return self._name
    def set_name (self, name):
        if type(name) == str and len(name) > 0 and len(name) < 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_job (self):
        return self._job
    def set_job (self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        elif job in APPROVED_JOBS:
            self._job = job

    name = property(get_name, set_name)
    job = property(get_job, set_job)
    pass