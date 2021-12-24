# each next number equals the sum of the previous two 

n1 = n2 = 1
n = 10
for i in range(2, n):
    n1, n2 = n2, n1 + n2
    print(n2)