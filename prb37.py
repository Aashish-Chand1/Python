# List of words for numbers from 0 to 19
number_words = [
    "zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine", 
    "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

num = int(input("Enter a number (0 to 19): "))

if 0 <= num <= 19:
    print(f"The number {num} in words is '{number_words[num]}'.")
else:
    print("Error: Please enter a number between 0 and 19.")
