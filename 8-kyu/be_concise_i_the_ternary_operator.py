def describe_age(a):
    return "You're a(n) "+("kid"*(a<=12)or"teenager"*(a<=17)or"adult"*(a<=64)or"elderly")
