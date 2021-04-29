from math import factorial

'''
n1 dices, the possibility where you
'''


def combination(n,m):
    if n < m:
        raise ValueError
    else:
        return factorial(n)/(factorial(m)*factorial(n-m))


def fun(n_1, n_2, k_1, k_2, k_3, k_4, k_5, k_6):
    if k_1 + k_2 + k_3 + k_4 + k_5 + k_6 != n_2:
        raise ValueError
    else:
        sum = 0
        for m_1 in range(k_1, n_1 - n_2 + k_1 + 1):
            for m_2 in range(k_2, n_1 - n_2 + k_1 + 1 - m_1 + k_2):
                for m_3 in range(k_3, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3):
                    for m_4 in range(k_4, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3 - m_3 + k_4):
                        for m_5 in range(k_5, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3 - m_3 + k_4 - m_4 + k_5):
                            m_6 = n_1 - m_1 - m_2 - m_3 - m_4 - m_5
                            sum += combination(n_1, m_1) * combination(n_1 - m_1, m_2) * combination(n_1 - m_1 - m_2, m_3) * \
                                    combination(n_1-m_1-m_2-m_3, m_4) * combination(n_1-m_1-m_2-m_3-m_4, m_5)
    result = sum/(6**n_1)
    return result


def fun_two(n_1, pattern: list):
    n_2 = sum(pattern)
    dice_face_number = len(pattern)
    summer = 0
    for i in range(dice_face_number):
    for m_1 in range(k_1, n_1 - n_2 + k_1 + 1):
        for m_2 in range(k_2, n_1 - n_2 + k_1 + 1 - m_1 + k_2):
            for m_3 in range(k_3, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3):
                for m_4 in range(k_4, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3 - m_3 + k_4):
                    for m_5 in range(k_5, n_1 - n_2 + k_1 + 1 - m_1 + k_2 - m_2 + k_3 - m_3 + k_4 - m_4 + k_5):
                        m_6 = n_1 - m_1 - m_2 - m_3 - m_4 - m_5
                        summer += combination(n_1, m_1) * combination(n_1 - m_1, m_2) * combination(n_1 - m_1 - m_2, m_3) * \
                                combination(n_1-m_1-m_2-m_3, m_4) * combination(n_1-m_1-m_2-m_3-m_4, m_5)
    result = summer/(6**n_1)


if __name__ == '__main__':
    ans = fun(3, 2, 0, 0, 0, 0, 0, 2)
