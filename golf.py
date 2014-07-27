def golf(number):
    i = number + 1
    result = i
    while True:
        if isPrime(i): and isPalindrome(i):
            result = i
            break
        i += 1
    return result

def isPrime(number):
    flag = True
    for i in range(2,number):
        if number%i == 0:
            flag = False
            break

    return flag

def isPalindrome(number):
    number = str(number)
    return number == number[::-1]
    #flag = True
    #if len(str(number)) != 1:
    #    sn = str(number)
    #    for i in range(int(len(sn)/2)):
    #        if sn[i] != sn[(i*-1)-1]:
    #            flag = False
    #            break
    #return flag