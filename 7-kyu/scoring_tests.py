def score_test(tests, right, omit, wrong):
    count_right = tests.count(0)
    count_omit = tests.count(1)
    count_wrong = tests.count(2)
    return count_right * right + count_omit * omit - count_wrong * wrong
