def arrays_similar(seq1, seq2):
    seq1_num = [i for i in seq1 if isinstance(i, (int, float))]
    seq1_str = [i for i in seq1 if not isinstance(i, (int, float))]
    seq2_num = [i for i in seq2 if isinstance(i, (int, float))]
    seq2_str = [i for i in seq2 if not isinstance(i, (int, float))]
    
    return sorted(seq1_num) == sorted(seq2_num) and sorted(seq1_str) == sorted(seq2_str)