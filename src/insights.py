from src.jobs import read


def get_unique_job_types(path):
    job_by_type = read(path)
    job = set()
    for types in job_by_type:
        job.add(types["job_type"])
    return list(job)


def filter_by_job_type(jobs, job_type):
    list_jobs = list()
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    industries = read(path)
    industry_type = set()
    for industry in industries:
        if len(industry["industry"]) != 0:
            industry_type.add(industry["industry"])
    return list(industry_type)


def filter_by_industry(jobs, industry):
    list_industries = list()
    for job in jobs:
        if job["industry"] == industry:
            list_industries.append(job)
    return list_industries


def get_max_salary(path):
    max_salary = read(path)
    all_salaries = list()
    for salary in max_salary:
        if len(salary["max_salary"]) != 0 and salary["max_salary"].isnumeric():
            all_salaries.append(int(salary["max_salary"]))
    return max(all_salaries)


def get_min_salary(path):
    min_salary = read(path)
    all_salaries = list()
    for salary in min_salary:
        if len(salary["min_salary"]) != 0 and salary["min_salary"].isnumeric():
            all_salaries.append(int(salary["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
