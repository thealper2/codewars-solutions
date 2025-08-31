from preloaded import CARS

def find_misfire(string):
    make, engine, sequence = string.split()
    correct_order = CARS[make][engine]
    current_cylinders = sequence.split('-')
    correct_cylinders = correct_order.split('-')
    misfires = []
    for i in range(len(correct_cylinders)):
        if current_cylinders[i] == 'X':
            misfires.append(correct_cylinders[i])
            
    return '-'.join(misfires)
