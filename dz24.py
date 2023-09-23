n = int(input())
a = list(map(int, input().split()))

max_sum = 0
for i in range(n):
    curr_sum = a[i] + a[(i+1)%n] + a[(i+2)%n]
    max_sum = max(max_sum, curr_sum)

print(max_sum)
