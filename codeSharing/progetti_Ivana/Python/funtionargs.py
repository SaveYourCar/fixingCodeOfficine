def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

a = 7
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"

for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")


try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)