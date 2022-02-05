#string length
'''
fruit = 'banana'
print(len(fruit))
'''
#len function
'''
fruit = 'banana'
x = len(fruit)
print(x)
'''
#looping thru strings
'''
fruit = 'banana'
index =0 
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    '''
'''
fruit = 'banana'
for letter in fruit:
    print(letter)
    '''
#looping and counting
'''
word = 'banana'
count = 0
for letter in word :
    if letter == 'n' :
        count = count + 1
print(count)
'''
#using in value
'''
for letter in 'banana' :
    print(letter)
    '''
#slicing strings
'''
s = 'monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
'''
#searching a string
'''
fruit = 'banana'
pos = fruit.find('a')
print(pos)
'''
# upper case
'''
greet = 'Hello Roy'
pos = greet.upper()
print(pos) 
'''
#lower case
'''
greet = 'Hello Roy'
pos = greet.lower()
print(pos) 
'''
#replace
'''
greet = 'Hello Roy'
pos = greet.replace('Roy','john')
print(pos)
'''
#stripping whitespace
'''
greet = '  Hello Roy  '
greet.strip()
print(greet) 
'''
#exercise1

str = 'X-DSPAM-Confidence: 0.8475'

pos = str.find(':')
#print(pos)
piece = str[pos+2:]
#print(piece)
value = float(piece)
print(value)

