def resistor_parallel(*args):
    resistors = list(args)
    return 1 / sum(1 / resistor for resistor in resistors)
