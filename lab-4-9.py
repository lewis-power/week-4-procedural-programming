def are_anagrams(a, b):
    return sorted(a.upper()) == sorted(b.upper())

first = input("Enter the first word: ")
second = input("Enter the second word: ")
print(are_anagrams(first, second))
