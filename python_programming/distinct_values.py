import flask_sqlalchemy
from flask_sqlalchemy import xrange

A = [4, 5, 6, 3, 2, 4]


def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for k in xrange(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result


print(distinct(A))
