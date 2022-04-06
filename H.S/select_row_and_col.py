n, m = map(int, input().split())
rows = [0] * n
cols = [0] * m
board = []
for i in range(n):
    nums = list(map(int, input().split()))
    board.append(nums)
    rows[i] = sum(nums)
    for j in range(m):
        cols[j] += nums[j]
mx = -1
for i in range(n):
    for j in range(m):
        pivot_sum = rows[i] + cols[j] - board[i][j]
        mx = max(mx, pivot_sum)
print(mx)
