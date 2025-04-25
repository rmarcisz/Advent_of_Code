from collections import Counter

def MinWindowSubstring(strArr):
    base, target = strArr[0], strArr[1]
    tgt_let = Counter(target)
    right, left = 0, 0
    words = []
    word = base[left:right]

    while right < len(base):
        right += 1
        word = base[left:right]
        word_let = Counter(word)
        while all(word_let.get(key, -1) >= val for key, val in tgt_let.items()):
            left += 1
            word = base[left:right]
            word_let = Counter(word)
            if any(word_let.get(key, -1) < val for key, val in tgt_let.items()):
                words.append([left -1, right])
    min_len = len(base)
    for res in words:
        min_len = min(len(base[res[0]:res[1]]), min_len)
    return min_len
# keep this function call here
print((MinWindowSubstring(['radsssserkaaaaaaraddsadaerkaaaaaaaraderaaaaaa', 'raderk'])))