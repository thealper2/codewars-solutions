def dot(n,m):
    result = ['+---' * n + '+']
    for _ in range(m):
        result.append('| o ' * n + '|')
        result.append('+---' * n + '+')

    return '\n'.join(result)
