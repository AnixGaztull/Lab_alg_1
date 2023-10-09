table_ = [[1, 3, 7, 22],
          [2, 4, 8, 100],
          [27, 28, 80, 102]]
n = 4
m = 3
target = 81


def bin_search(target_, array, l_, r_):
    left_ = l_
    right_ = r_
    while left_ < right_:
        mid_ = (left_ + right_) // 2
        if array[mid_] < target_:
            left_ = mid_ + 1
        else:
            right_ = mid_
    if array[left_] == target_: return left_
    return left_ - 1


def exponential_search(target_, array, k):
    ind_ = k - 1
    diff_ = 1
    while ind_ >= 0 and array[ind_] > target_:
        ind_ -= diff_
        diff_ *= 2
    return bin_search(target_, array, max(ind_, 0), max(ind_, 0) + (diff_ // 2))


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
        curr_j = exponential_search(target, table_[curr_i], curr_j + 1)
print(answ_)
