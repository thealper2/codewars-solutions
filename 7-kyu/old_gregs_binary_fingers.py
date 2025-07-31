def binary_fingers(bin_string):
    finger_names = ["Pinkie", "Ring", "Middle", "Index", "Thumb"]
    result = []
    padded_bin = bin_string.zfill(5)
    relevant_bits = padded_bin[-5:]
    for i in range(5):
        if i < len(relevant_bits) and relevant_bits[i] == "1":
            result.append(finger_names[i])

    return result
