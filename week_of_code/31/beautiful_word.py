def is_beautiful_word(word):
    vowels = "aeiouy"
    for c1, c2 in zip(word, word[1:]):
        if c1 == c2 or (c1 in vowels and c2 in vowels):
            return False
    return True


w = input().strip()
if is_beautiful_word(w):
    print("Yes")
else:
    print("No")
