table_ = [[1, 3, 7, 22],
          [2, 4, 8, 100],
          [27, 28, 80, 102]]
n = 4
m = 3
target = 22
curr_i = 0
curr_j = n - 1
answ_ = False
while curr_i < m and curr_j >= 0:
    if table_[curr_i][curr_j] == target:
        answ_ = True
        break
    if table_[curr_i][curr_j] < target:
        curr_i += 1
    elif table_[curr_i][curr_j] > target:
        curr_j -= 1
print(answ_)
