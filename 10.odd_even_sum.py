num = int(input())

even_sum = 0
odd_sum = 0
Diff = 0

for i in range(1, num+1):
    n = int(input())
    if i % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    Diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {Diff}")
