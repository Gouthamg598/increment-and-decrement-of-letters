'''===============increment==================='''

# t=int(input('enter test cases:'))
# for i in range(t):
#     a=input('\nenter any string:')
#     b=int(input('\nenter increment:'))
#     for i in (a):
#         c=ord(i)+b
#         if c>=97 and c<=122:
#             print(chr(c),end='')
#         else:
#             c=c-122+96
#             print(chr(c),end='')
'''================decrement================'''
t=int(input('enter test cases:'))
for i in range(t):
    a=input('\nenter any string:')
    b=int(input('\nenter decrement:'))
    for i in (a):
        c=ord(i)-b
        if c>=97 and c<=122:
            print(chr(c),end='')
        else:
            c=123-97+c
            print(chr(c),end='')
