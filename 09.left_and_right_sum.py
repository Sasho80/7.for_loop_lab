num = int(input())

left_sum = 0
right_sum = 0
diff = 0

for i in range(1, 2 * num+1):
    n = int(input())
    if i <= (2 * num+1)/2:
        left_sum += n
    else:
        right_sum += n

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")
