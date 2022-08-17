from src.sorting import sort_by


jobs = [
    {
        "date_posted": "2022-08-17",
        "max_salary": 1000,
        "min_salary": 100,
    },
    {
        "date_posted": "2022-07-17",
        "max_salary": 100,
        "min_salary": 10,
    },
    {
        "date_posted": "2022-09-17",
        "max_salary": 10000,
        "min_salary": 1000,
    }
]


criteria_min_salary = [
    jobs[1],
    jobs[0],
    jobs[2]
]

criteria_max_salary = [
    jobs[2],
    jobs[0],
    jobs[1]
]

criteria_max_salary_and_date_posted = [
    jobs[2],
    jobs[0],
    jobs[1]
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == criteria_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == criteria_max_salary

    sort_by(jobs, "max_salary")
    assert jobs == criteria_max_salary_and_date_posted
