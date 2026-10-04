class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state

    def transition(self, symbol):
        return self.transitions[symbol]


class Automaton:
    def __init__(self, start_state, accept_state):
        self.start_state = start_state
        self.accept_state = accept_state

    def read_commands(self, commands):
        current = self.start_state

        for command in commands:
            current = current.transition(command)

        return current == self.accept_state


q1 = State("q1")
q2 = State("q2")
q3 = State("q3")

q1.add_transition("0", q1)
q1.add_transition("1", q2)

q2.add_transition("0", q3)
q2.add_transition("1", q2)

q3.add_transition("0", q2)
q3.add_transition("1", q2)

my_automaton = Automaton(q1, q2)