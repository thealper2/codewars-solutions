def gc_content(seq):
    if not seq:
        return 0.0

    return ((seq.count("C") + seq.count("G")) / len(seq)) * 100
