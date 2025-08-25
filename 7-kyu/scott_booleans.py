false = lambda f: lambda t: f
true = lambda f: lambda t: t
iff = lambda b: lambda x: lambda y: b(y)(x)
