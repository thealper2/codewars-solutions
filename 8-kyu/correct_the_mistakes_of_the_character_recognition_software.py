def correct(s):
    db = {"S": "5", "0": "O", "1": "I",
          "5": "S", "O": "0", "I": "1"}
    return ''.join([db.get(_, _) for _ in s])