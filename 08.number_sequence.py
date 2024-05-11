import sys

smallest = sys.maxsize
biggest = -sys.maxsize
next_num = 0

num = int(input())

for i in range(1, num + 1):
    n = int(input())
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
