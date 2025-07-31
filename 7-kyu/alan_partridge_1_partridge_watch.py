def part(arr):
    terms = ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    total_marks = sum([1 for word in arr if word in terms])
    if not total_marks:
        return "Lynn, I've pierced my foot on a spike!!"
    
    return "Mine's a Pint" + "!" * total_marks
