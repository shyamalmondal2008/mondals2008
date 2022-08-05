X = ['xyz','xyz1','abc','abc1','cde']
Y = ["NOT OK", "OK", "ERROR", "OK"]

def isalphanumeric(P,Q):
    count_p = 0
    count_q = 0
    result = 0
    for i in P:
        if i.isalpha():
            count_p += 1
    for j in Q:
        if j == "OK":
            count_q += 1
    print(count_p)
    result = count_q * 100/count_p
    return result



print("result is.....",isalphanumeric(X,Y))
