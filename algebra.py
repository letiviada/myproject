from math import gcd
from itertools import product

counter = 0

def lcm(element):
    output = 1
    for i in element:
        output = output*i//gcd(output, i)
    return output


def c(n): # cyclic group
    listOfOrders = [int(n/gcd(x, n)) for x in range(1, n+1)]
    return listOfOrders


def directProduct(groups, order):

    counter = 0
    
    for combination in product(*groups):
        #print(combination)
        #print(lcm(combination))
        if lcm(combination) == order:
            counter += 1

    return counter

groupsInvolved = [c(35),c(25*4*121*49*7)] # groups in direct product
desiredOrder = 5 # order of element required
print(directProduct(groupsInvolved, desiredOrder)) #answer
