def create_commutator(a: str, b: str) -> str:
    a_turns = a.split()
    b_turns = b.split()
    
    def reverse_turn(turn):
        if "'" in turn:
            return turn.replace("'", "")
        elif "2" in turn:
            return turn
        else:
            return turn + "'"
        
    a_rev = [reverse_turn(turn) for turn in a_turns[::-1]]
    b_rev = [reverse_turn(turn) for turn in b_turns[::-1]]
    result = a_turns + b_turns + a_rev + b_rev
    return ' '.join(result)
