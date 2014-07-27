def golf(n):
    r = i = n + 1
    while True:
        if p(i) and pl(str(i)): r = i; break
        i+=1
    return r
def p(n):
    for i in range(2,n):
        if n%i == 0: return False
    return True
def pl(n):
    return n == n[::-1]