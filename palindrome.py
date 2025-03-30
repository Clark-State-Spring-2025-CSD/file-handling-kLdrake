#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

wordlist = open("words.txt")

count = 0

for line in wordlist:
    words = line.lower().split()
    count += sum(w == w[::-1] for w in words)

wordlist.close()

print(f"There are {count} palindromes.")

