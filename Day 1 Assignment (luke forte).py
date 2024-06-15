import math
import random

# 1
f = lambda x: x // 1
c = lambda x: x // 1 + 1

# 2
num = input('Pick a 2 digit number...')
int(num[::-1])

# 3
name = input('Your Name is...')
"You have a nice name." if name == 'luke' or 'John Cleese' or 'Michael Palin' else "It was Nice to meet you."

# 4
originalPrices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = .6
for x in originalPrices:
    print('Original Price: $', x)
    print('Discount:', discount * 100, '%')
    finalPrice = math.floor((x * discount) * 100) / 100
    print('Final Price: $', finalPrice)


# 5
length = 5
print('a', 'b', 'pow(a,b)')
for i in range(1, length+1):
    print(i, i+1, end=' ')
    power = 1
    for j in range(i+1):
        power *= i
    print(power)


# 6
guess = input('input 3 numbers...')
guess = list(guess)
amt = 0
winningNum = random.randint(100, 1000)
print('Winning Numbers:', winningNum)
winningNum = list(str(winningNum))
if guess == winningNum:
    print('Congratulations, you just won $10000!')
else:
    for x in guess:
        x = x
        if x in winningNum:
            amt += 1
    if amt == 1:
        print('Congratulations, you just won $1000!')
    elif amt == 3:
        print('Congratulations, you just won $3000!')
    else:
        print('Better luck next time!')


# 7
numbers = input()
numbers = list(numbers)
print('Numbers:', numbers)
numbers.sort(key=int, reverse=True)
print('The highest value', numbers[0])
print('Occurrences:', numbers.count(numbers[0]))

#8
def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
triangle(5)

#9
size = 7
for i in range(1, size + 1):
    print(' '*i,end='')
    for j in range(i, size+1):
        print(j, end=' ')
    print()

for i in range(size - 1, 0, -1):
    print(' '*i,end='')
    for j in range(i, size+1):
        print(j, end=' ')
    print()

#10
phoneNumber = input('Number:')
num = str()
for char in phoneNumber:
   if(char.lower() in 'abc'):
       num += '2'
   elif(char.lower() in 'def'):
       num += '3'
   elif(char.lower() in 'ghi'):
       num += '4'
   elif(char.lower() in 'jkl'):
       num += '5'
   elif(char.lower() in 'mno'):
       num += '6'
   elif(char.lower() in 'pqrs'):
       num += '7'
   elif(char.lower() in 'tuv'):
       num += '8'
   elif(char.lower() in 'wxyz'):
       num += '9'
   else:
       num += char

print(num)




