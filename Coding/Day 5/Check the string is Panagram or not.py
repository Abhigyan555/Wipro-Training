text = "The quick brown fox jumps over the lazy dog"

abc = "abcdefghijklmnopqrstuvwxyz"

for ch in abc:
    if ch not in text:
        print("Not a Pangram")
        break
else:
    print("It is a Pangram")
