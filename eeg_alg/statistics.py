def relative_frequency(data):
    freq = dict()
    s = 0

    for d in data:
        s += d
        if d not in freq:
            freq[d] = 0
        freq[d] += d

    for key in freq.keys():
        freq[key] /= s

    return freq
