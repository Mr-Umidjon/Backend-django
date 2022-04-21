### x = ((i + j)*(j+45))/(10-i)

from add import add_numbers
from sub import sub_numbers
from mul import mul_numbers
from div import div_numbers

i = float(input("I = "))
j = float(input("J = "))

x = div_numbers(mul_numbers(add_numbers(i, j), add_numbers(j, 45)), sub_numbers(10, i))
print(x)
print(((i + j)*(j+45))/(10-i))
