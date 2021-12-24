def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1)*n

fc = int(input())
print('Factorial {} equals {}'.format(fc, factorial(fc)))

fact = 1
while fc > 0:
    fact *= fc
    fc -= 1
print(fact)