def decompose_single_strand(single_strand):
    n = len(single_strand)
    frame1 = "Frame 1: " + " ".join([single_strand[i : i + 3] for i in range(0, n, 3)])
    frame2 = "Frame 2: " + " ".join(
        [single_strand[:1]] + [single_strand[i : i + 3] for i in range(1, n, 3)]
    )
    frame3 = "Frame 3: " + " ".join(
        [single_strand[:2]] + [single_strand[i : i + 3] for i in range(2, n, 3)]
    )
    return "\n".join([frame1, frame2, frame3])
