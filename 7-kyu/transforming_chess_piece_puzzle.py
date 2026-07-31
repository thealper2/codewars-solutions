from collections import deque

CORNERS = {(0, 0), (0, 4), (4, 0), (4, 4)}
NEXT = {'r': 'b', 'b': 'q', 'q': 'r'}

def _moves(piece, r, c):
    """All destination squares for the piece from (r, c) on a 5x5 board."""
    dests = []
    if piece in ('r', 'q'):
        for i in range(5):
            if i != c: dests.append((r, i))
            if i != r: dests.append((i, c))
    if piece in ('b', 'q'):
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            nr, nc = r + dr, c + dc
            while 0 <= nr < 5 and 0 <= nc < 5:
                dests.append((nr, nc))
                nr += dr; nc += dc
    return dests

_states = [(p, r, c) for p in 'rbq' for r in range(5) for c in range(5)]

_successors = {}
_has_win = {}
for s in _states:
    p, r, c = s
    succ, win_now = [], False
    for (r2, c2) in _moves(p, r, c):
        if (r2, c2) in CORNERS:
            win_now = True
        else:
            succ.append((NEXT[p], r2, c2))
    _successors[s] = succ
    _has_win[s] = win_now

_preds = {s: [] for s in _states}
for s in _states:
    for t in _successors[s]:
        _preds[t].append(s)

_result = {}
_degree = {}
_queue = deque()

for s in _states:
    if _has_win[s]:
        _result[s] = 'win'
        _queue.append(s)
    else:
        _degree[s] = len(_successors[s])
        if _degree[s] == 0:
            _result[s] = 'lose'
            _queue.append(s)

while _queue:
    t = _queue.popleft()
    rt = _result[t]
    for s in _preds[t]:
        if s in _result:
            continue
        if rt == 'lose':
            _result[s] = 'win'
            _queue.append(s)
        else:
            _degree[s] -= 1
            if _degree[s] == 0:
                _result[s] = 'lose'
                _queue.append(s)

for s in _states:
    _result.setdefault(s, 'draw')

def transforming_chess(starting_piece, starting_row, starting_column):
    return _result[(starting_piece, starting_row, starting_column)]
