class Plugboard(object):
    def __init__(self, wires=''):
        """
        wires: This is the mapping of pairs of characters
        """
        if len(wires) % 2 != 0:
            raise ValueError("Wires must come in pairs")

        if len(wires) > 20:
            raise ValueError("Too many wires (maximum is 10)")

        self.mapping = {}
        seen = set()
        for i in range(0, len(wires), 2):
            a, b = wires[i], wires[i + 1]
            if a < 'A' or a > 'Z' or b < 'A' or b > 'Z':
                raise ValueError("Only uppercase letters A-Z allowed")

            if a == b:
                raise ValueError("A letter cannot be wired to itself")

            if a in seen or b in seen:
                raise ValueError("Each letter can only appear once")

            seen.add(a)
            seen.add(b)
            self.mapping[a] = b
            self.mapping[b] = a

    def process(self, c):
        """
        c: The single character to process
        """
        return self.mapping.get(c, c)
