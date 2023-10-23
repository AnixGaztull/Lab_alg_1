import matplotlib.pyplot as plt
import time

n = 2 ** 13


def generate_data(m_table, type_table):
    table_ = [[0] * n for row_ in range(m)]
    for i in range(m_table):
        for j in range(n):
            if type_table == 1:
                table_[i][j] = (n // m * i + j) * 2
            else:
                table_[i][j] = (n // m * i * j) * 2
    if type_table == 1:
        target_ = n * 2 + 1
    else:
        target_ = 16 * n + 1

    return table_, target_


################################################

def first_alg(curr_table, curr_target):
    curr_i = 0
    curr_j = n - 1
    answ_ = False
    while curr_i < m and curr_j >= 0:
        if curr_table[curr_i][curr_j] == curr_target:
            answ_ = True
            break
        if curr_table[curr_i][curr_j] < curr_target:
            curr_i += 1
        elif curr_table[curr_i][curr_j] > curr_target:
            curr_j -= 1
    return answ_


################################################
def bin_search_second_alg(curr_target, array, n_):
    left_ = 0
    right_ = n_ - 1
    while left_ < right_:
        mid_ = (left_ + right_) // 2
        if array[mid_] < curr_target:
            left_ = mid_ + 1
        else:
            right_ = mid_
    return left_


def second_alg(curr_table, curr_target):
    answ_ = False
    for i in range(m):
        t = bin_search_second_alg(target, curr_table[i], n)
        if curr_table[i][t] == curr_target:
            answ_ = True
            break
    return answ_


####################################################
def bin_search_third_alg(curr_target, array, l_, r_):
    left_ = l_
    right_ = r_
    while left_ < right_:
        mid_ = (left_ + right_) // 2
        if array[mid_] < curr_target:
            left_ = mid_ + 1
        else:
            right_ = mid_
    if array[left_] == curr_target: return left_
    return left_ - 1


def exponential_search_third_alg(curr_target, array, k):
    ind_ = k - 1
    diff_ = 1
    while ind_ >= 0 and array[ind_] > curr_target:
        ind_ -= diff_
        diff_ *= 2
    return bin_search_third_alg(curr_target, array, max(ind_, 0), max(ind_, 0) + (diff_ // 2))


def third_ald(curr_table, curr_target):
    curr_i = 0
    curr_j = n - 1
    answ_ = False
    while curr_i < m and curr_j >= 0:
        if curr_table[curr_i][curr_j] == curr_target:
            answ_ = True
            break
        if curr_table[curr_i][curr_j] < curr_target:
            curr_i += 1
        elif curr_table[curr_i][curr_j] > curr_target:
            curr_j = exponential_search_third_alg(curr_target, curr_table[curr_i], curr_j + 1)
    return answ_


################################################
th_1 = []
th_2 = []
for type_ in range(2):
    m = 1
    X = []
    Y_1 = []
    Y_2 = []
    Y_3 = []
    for power_ in range(0, 14):
        table, target = generate_data(m, type_ + 1)
        X.append(power_)

        start_time = time.time()
        a = first_alg(table, target)
        end = time.time()
        t = end - start_time
        s = (end - start_time) * 1000
        Y_1.append(s)

        start_time = time.time()
        a = second_alg(table, target)
        end = time.time()
        s = (end - start_time) * 1000
        Y_2.append(s)

        start_time = time.time()
        a = third_ald(table, target)
        end = time.time()
        s = (end - start_time) * 1000
        Y_3.append(s)
        if not type_:
            th_1.append(s)
        else:
            th_2.append(s)
        m *= 2
    plt.figure(figsize=(16, 6))
    plt.plot(X, Y_1)
    plt.plot(X, Y_2)
    plt.plot(X, Y_3)
    plt.ylabel('Time,[ms]')
    plt.xlabel('M, 2**M')
    x_ticks = [k for k in range(1, 14)]
    x_labels = [k for k in range(1, 14)]
    plt.xticks(x_ticks, x_labels)
    plt.yticks(minor=True)
    plt.legend(['1st alg, (N+M)', '2nd alg, M*logN', '3rd alg, M(logN-logM+1)'])
    plt.grid()
    print("1st alg[mc]:")
    print('\n'.join(list(map(str, Y_1))))
    print("2nd alg[mc]:")
    print('\n'.join(list(map(str, Y_2))))
    print("3rd alg[mc]:")
    print('\n'.join(list(map(str, Y_3))))
plt.figure(figsize=(16, 6))
plt.plot(X, th_1)
plt.plot(X, th_2)
plt.ylabel('Time,[ms]')
plt.xlabel('M, 2**M')
plt.xticks([k for k in range(1, 14)])
plt.yticks(minor=True)
plt.grid()
plt.legend(['1st type of data', '2nd type of data'])
plt.show()
