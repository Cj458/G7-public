"""
Function: it's a named block of code which does a specific thing.
Terms:
1. define: it's a keyword for creating a function -> def
2. call: to use a function
3. parameter: these are info that we pass to the func to use
4. return: 

"""

# example
print(2)


# input()

# max()
# min()

# to create a func, use def keyword followed by the name of the func.
# then round brackets(), followed by colon(:)

def func_name(name) -> None:
    print(f'Hello from the {name} func')

func_name(9)

def add(x, y):
    return  x+y


def subst(x, y):
    return x-y

def mult(x, y):
   return x*y

def div(x, y):
    return x/y


print(add(5, 5))

res = add(5, 5)
sub = subst(5, 5)
mul = mult(5, 5)
di = div(5, 5)

print('this is the res' ,res*2)
print('this is the sub' ,sub*2)
print('this is the mul' ,mul*2)
print('this is the div' ,di*2)



input()
max()
min()
round()