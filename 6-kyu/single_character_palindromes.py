def solve(s):
	if s == s[::-1]:
		return 'OK'

	n = len(s)
	for i in range(n):
		new_s = s[:i] + s[i + 1:]
		if new_s == new_s[::-1]:
			return 'remove one'

	return 'not possible'
