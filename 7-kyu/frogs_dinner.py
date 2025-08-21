def summation(n):
    return (n * (n + 1)) // 2

def frog_contest(flies):
    chris_ate = summation(flies)
    tom_ate = summation(chris_ate // 2)
    cat_ate = summation(chris_ate + tom_ate)
    return f"Chris ate {chris_ate} flies, Tom ate {tom_ate} flies and Cat ate {cat_ate} flies"
