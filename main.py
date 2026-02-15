# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        s += i
print(s)

# 2
n = int(input())
product = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        product *= i
print(product)

# 3
n = int(input())
largest = -10**9
second = -10**9
for i in range(n):
    x = int(input())
    if x > largest:
        second = largest
        largest = x
    elif x > second:
        second = x
print(second)

# 4
n = int(input())
smallest = 10**9
second_small = 10**9
for i in range(n):
    x = int(input())
    if x < smallest:
        second_small = smallest
        smallest = x
    elif x < second_small:
        second_small = x
print(second_small)

# 5
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)
