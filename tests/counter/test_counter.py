from src.counter import count_ocurrences


def test_counter():
    report_JS = count_ocurrences("src/jobs.csv", "Javascript")
    report_PY = count_ocurrences("src/jobs.csv", "Python")

    assert report_JS == 122
    assert report_PY == 1639
