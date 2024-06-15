#1

"""Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers.Within
each group the numbers should be displayed in the same order that they were entered
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line.
page 4-7 day 2 notes"""

run = 0
pos = []
neg = []
zero = []
while run == 0:
    x = input('enter a number...')
    #for n in x:
    if x == "":
       run = 1
    elif int(x) < 0:
        neg.append(x)
    elif int(x) == 0:
        zero.append(x)
    elif int(x) > 0:
        pos.append(x)
fin = neg + zero + pos
for z in fin:
    print (z)

#2
"""Evaluating a postfix expression is easier than evaluating an infix expression because it
does not contain any brackets and there are no operator precedence rules to consider.
A postfix expression can be evaluated using the following algorithm:

	Create a new empty list, values
	For each token in the postfix expression
	If the token is a number then
	Convert it to an integer and add it to the end of values
	Else
	Remove an item from the end of values and call it right
	Remove an item from the end of values and call it left
	Apply the operator to left and right
	Append the result to the end of values
	Return the first item in values as the value of the expression

Write a program that reads a mathematical expression in postfix form from the user,
evaluates it, and displays its value.
[ if you dont know what is postfix expression, you can get more information about postfix in google,still if you dont
understand , you can message me in skype,i will help u]"""


inp = input('input:')
inp = list(inp)
global l
l = []
for x in inp:
    if x.isdigit():
        l.append(int(x))
    elif x == "":
        break
    else:
        op = x
        lst = l[-1]
        l.pop()
        fst = l[-1]
        l.pop()
        l.append(str(eval(str(fst) + x + str(lst))))
print (l)