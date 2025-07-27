def missing(nums, s):
    nums.sort()
    letters_only = s.replace(" ", "")
    for index in nums:
        if index >= len(letters_only):
            return "No mission today"

    word = ''.join([letters_only[i].lower() for i in nums])
    return word