def job_matching(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']