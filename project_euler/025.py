# Find the first Fib number containig 1000 digits.
# Using dynamic programming
top = 100000000
F = [0 for i in range(top)]
F[1] = 1
F[2] = 1
F[3] = 2
i = 3

while (int(len(str(F[i]))) != 1000):
    i += 1
    F[i] = F[i-1] + F[i-2]

print("Fib(" + str(i) + ") = " + str(F[i]))
#Fib(4782) ...
