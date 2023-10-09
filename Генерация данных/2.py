n = 2 ** 13


def generate_data(m_table):
    table_ = [[0] * n for row_ in range(m_table)]
    for i in range(m_table):
        for j in range(n):
            table_[i][j] = (n // m_table * i * j) * 2
    target_ = n * 16 + 1
    return table_, target_


m = int(input())
t = 2 ** m
data, target = generate_data(t)
print(data)
