table_ = [[1, 3, 7, 22],
          [2, 4, 8, 100],
          [27, 28, 80, 102]]
n = 4
m = 3
target = 28


def bin_search(target_, array, n_):
    left_ = 0
    right_ = n_-1
    while left_ < right_:
        mid_ = (left_ + right_) // 2
        if array[mid_] < target_:
            left_ = mid_+1
        else:
            right_ = mid_
    return left_


answ_ = False
for i in range(m):
    t = bin_search(target, table_[i], n)
    if table_[i][t] == target:
        answ_ = True
        break
print(answ_)
