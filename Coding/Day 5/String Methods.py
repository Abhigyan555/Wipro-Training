text = "  hello World  "

print("Original Text:", text)

# 1. lower()
print("Lowercase:", text.lower())

# 2. upper()
print("Uppercase:", text.upper())

# 3. strip()
print("Strip spaces:", text.strip())

# 4. title()
print("Title case:", text.title())

# 5. replace()
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# 6. find()
print("Find position of 'World':", text.find("World"))

# 7. count()
print("Count of 'l':", text.count("l"))

# 8. startswith()
print("Starts with '  hello':", text.startswith("  hello"))

# 9. endswith()
print("Ends with 'World  ':", text.endswith("World  "))

# 10. split()
print("Split into words:", text.split())

# 11. join()
words = ['Python', 'is', 'fun']
print("Join words with space:", " ".join(words))
