# Question 5

P = 10000
n = 12
r = 8/100

t = int(input("What is the time duration? "))

a = P * (1 + r/n) ** n * t
print("The amount after " + str(t) + " years is " + str(a))