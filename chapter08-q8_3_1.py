from collections import Counter
def find_unique_character(s):
    counts = Counter(s)
    unique_chars = [char for char, count in counts.items() if count == 1]
    return unique_chars

test_string = "abacbad"
print(find_unique_character(test_string))
