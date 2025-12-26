import time

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0 or m > n:
        return 0
    
    last = {}
    for i in range(m):
        last[pattern[i]] = i

    count = 0
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            count += 1
            i += m

        else:
            ch = text[i + j]
            last_pos = last.get(ch, -1)
            shift = j - last_pos
            if shift < 1:
                shift = 1
            i += shift

    return count

def kmp(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0 or m > n:
        return 0
    
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    i = 0
    j = 0
    count = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                count += 1
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count

def rabin_karp(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0 or m > n:
        return 0
    
    base = 256
    mod = 10**9 + 7

    h = 1
    for _ in range(m - 1):
        h = (h * base) % mod

    pattern_hash = 0#
    window_hash = 0

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    count = 0

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                count += 1

        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * h) % mod
            window_hash = (window_hash * base + ord(text[i + m])) % mod
            window_hash %= mod
    return count

def choose_patterns(text):
    words = text.split()

    pattern_exist = None
    for w in words:
        w_clean = w.strip('.,!?:;"()[]«»')
        if len(w_clean) >= 5:
            pattern_exist = w_clean
            break

    if pattern_exist is None:
        pattern_exist = "test"

    pattern_fake = pattern_exist + "_xyz"

    return pattern_exist, pattern_fake

def measure(func, text, pattern, repeats=3):
    start = time.perf_counter()
    for _ in range(repeats):#
        func(text, pattern)#
    end = time.perf_counter()
    return (end - start) / repeats

def main():
    with open("article1.txt", "r", encoding="utf-8", errors="ignore") as f:
        text1 = f.read()

    with open("article2.txt", "r", encoding="utf-8", errors="ignore") as f:
        text2 = f.read()

    p1_exist, p1_fake = choose_patterns(text1)
    p2_exist, p2_fake = choose_patterns(text2)

    algorithms = [
        ("Boyer-Moore", boyer_moore),
        ("KMP",         kmp),
        ("Rabin-Karp",  rabin_karp),
    ]

    print("=== ТЕКСТ 1 (article1.txt) ===")
    print(f"Підрядок, який Є у тексті: '{p1_exist}'")
    for name, func in algorithms:
        t = measure(func, text1, p1_exist)
        print(f"{name:12s}: {t:.6f} c")

    print(f"\nПідрядок, якого НЕМАЄ у тексті: '{p1_fake}'")
    for name, func in algorithms:
        t = measure(func, text1, p1_fake)
        print(f"{name:12s}: {t:.6f} c")

    print("\n\n=== ТЕКСТ 2 (article2.txt) ===")
    print(f"Підрядок, який Є у тексті: '{p2_exist}'")
    for name, func in algorithms:
        t = measure(func, text2, p2_exist)
        print(f"{name:12s}: {t:.6f} c")

    print(f"\nПідрядок, якого НЕМАЄ у тексті: '{p2_fake}'")
    for name, func in algorithms:
        t = measure(func, text2, p2_fake)
        print(f"{name:12s}: {t:.6f} c")

if __name__ == "__main__":
    main()
