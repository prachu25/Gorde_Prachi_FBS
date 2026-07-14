# 02. Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = input('Enter any Alphabet: ')

if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
    print('Alphabet is VOWEL')
else:
    print('Alphabet is CONSONANT')



# Another Way 

"""
if alpha in "aeiou":
    print('Vowel')
else:
    print('Consonant')
"""
