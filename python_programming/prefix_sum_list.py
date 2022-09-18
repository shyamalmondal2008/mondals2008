def prefix_sums(A):
    n = len(A)
    P = [0] * n
    print("value of p is", P)
    P[0] = A[0]
    print("value of p is..........", P)
    print("value of p 0th positionn is........", P[0])
    for k in range(1, n):
        P[k] = P[k - 1] + A[k]
        print("new list for the loop is", P[k])
        print("new list for the loop is.....{}...{}".format( k, P))
    return P


print(prefix_sums([3, 4, 1, 6, 9]))
