#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

numbers = open("numbers.txt")

total = 0
avg = 0
count = 0
high = float('-inf')
low = float('inf')

for line in numbers:
    num = int(line)
    count += 1
    n = float(line)
    total += num
    if num > high:
        high = num
    if num < low:
        low = num

avg = total / count


numbers.close()

print(f"There are {count} numbers in the file.")
print(f"The average is {avg}.")
print(f"The highest number is {high}")
print(f"The lowest number is {low}")
