def detect_operator(num):
    operator_codes = {
        '039': 'Golden Telecom',
        '050': 'MTS',
        '063': 'Life:)',
        '066': 'MTS',
        '067': 'Kyivstar',
        '068': 'Beeline',
        '093': 'Life:)',
        '095': 'MTS',
        '096': 'Kyivstar',
        '097': 'Kyivstar',
        '098': 'Kyivstar',
        '099': 'MTS'
    }
    code = num[1:4]
    return operator_codes.get(code, "no info")