def check_connection(network, first, second):
    result = False
    
    if len(network) > 0:
        for n in network:
            if str(first) in str(n) and str(second) in str(n): 
                print(1)
                return True
            elif str(first) in str(n):
                print(2)
                r = n.split("-")
                first = r[1] if r[0] == first else r[0]
                network = getLid(network, n)
                result = check_connection(network, first, second)
                if result == True:
                    break
    return result
    
def getLid(network, n):
    new_tuple = []
    for s in list(network):
        if not s == n:
            new_tuple.append(s)
    return tuple(new_tuple)