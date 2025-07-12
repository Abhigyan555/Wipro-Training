text = "fifty five crore thirty four lakhs twenty three thousand two hundred and sixty seven"

nums = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
    'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    'hundred': 100, 'thousand': 1000, 'lakh': 100000, 'lakhs': 100000, 'crore': 10000000
}

words = text.split()
total = 0
temp = 0

for word in words:
    if word == 'and':
        continue
    elif word in nums:
        number = nums[word]
        if number < 100:
            temp += number
        else:
            temp *= number
            total += temp
            temp = 0

# Add remaining value
total += temp
print(text)
print("Final number is:", total)
