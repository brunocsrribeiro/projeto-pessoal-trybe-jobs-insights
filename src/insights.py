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
        if (
            len(salary["max_salary"]) != int
            and salary["max_salary"].isnumeric()
        ):
            all_salaries.append(int(salary["max_salary"]))
    return max(all_salaries)


def get_min_salary(path):
    min_salary = read(path)
    all_salaries = list()
    for salary in min_salary:
        if (
            len(salary["min_salary"]) != int
            and salary["min_salary"].isnumeric()
        ):
            all_salaries.append(int(salary["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Missing values.")
    elif (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("Non-numeric values.")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Invalid values")
    else:
        return job["min_salary"] <= salary and job["max_salary"] >= salary


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
