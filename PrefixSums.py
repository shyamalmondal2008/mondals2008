from flask_sqlalchemy import xrange


def prefix_sums(A):
    A = [2, 8, 9, 5, 7, 8]
    sums = [0] * (len(A)+1)
    print("sum is", sums)
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for k in xrange(1, n):
        P[k] = P[k - 1] + A[k]
    return P




