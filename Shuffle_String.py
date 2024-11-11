We have to read two strings as input and then print out another string that is a shuffled version of both strings. The string will have elements alternatively from both strings. 
S1 = BRING
S2 = camel

S1 = input()
S2 = input()
leng = len(S1)
result = ""
for char in range(0,leng):
    if char%2==0:
        result = result + S1[char]
    else:
        result = result + S2[char]
print(result)


Solution:

Read two inputs from the user let's say S1 and S2.
Create an empty string let's say result = "".
Find the length of the input S1 because both string's length is the same i.e, leng=len(S1).
Take for loop i with range (0, length) to get the characters from the index value 0 to the end length.
Inside the loop, check if i is even, i.e, if i%2==0: then concatenate the character at the i index of S1 to the result i.e, result=result+S1[i].
else, do concatenate the character at the i index of S2 to the result i.e, result=result+S2[i].
Print result.