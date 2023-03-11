import math # borrows someone else's math code
print("Pythagoras Theorem Calculator")
a = int(input("How big is a side a"))
b = int(input("How big is side b"))

c = math.sqrt(a*a + b*b)
print("The hypotenus is", c)

