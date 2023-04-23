# +
# -
# *
# /
# //
"""
1. Arithmetic operators.
 + : add
 - : substract
 * : multiply
 / : division with a floating point
 // : division without a floating point
 % : modulus -> remainder of a division
 eg. print(25%4) -> 1
"""
"""
exercise:
make a very simple calculator program.
useing the input(), ask a user to provide 2 numbers:
a and b or x and y, and ask them to tell you operation do they want to do.
+
-
/
* 
%
"""


# a = int(input('number a: '))
# b = int(input('number b: '))

# sign = input('operator: ')

# if sign == '+':
#     print(a+b)
# elif sign == '-':
#     print(a-b)
# elif sign == '/':
#     print(a/b)
# elif sign == '*':
#     print(a*b)
# elif sign == '%':
#     print(a%b)


"""
2. comparison operators

== : equal operator -> True/ False
!=  : not equal operator -> True/ False
< :  less than -> True/ False
>  :  great than -> True/ False
<= : less or equal -> True/ False
>= : great or equal -> True/ False

"""

a = 10
b = 5

"""
3. Membership operators

in -> checks the existence of something
not in -> checks non-existence of something

"""

x = '123456789'

print('0' not in x)


"""
4. logical operators

and: return True if both statements are true otherwise it returns False
or: return True if at least one statement if True and False if both statements are False

"""

a = 5
b = 10

x = 15
y = 20


print(a and b < y)