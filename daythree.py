


def sanitize(input):
    newinput = []
    for item in range(len(input)):
        newinput.append(input[item][:len(input[item])-1])
    return newinput


def gammaNum(input):
    output =0



    return

def epsilonNum(input ):
    output = 0


    return

def separateBits():
    file = open("inputdaythree1.txt", "r")
    input = file.readlines()
    file.close()
    newinput = sanitize(input)
    bits = [[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""]]
    for row in range(len(newinput)):
        for bit in range(len(newinput[row])):
            bits[bit][0] += newinput[row][bit]
    print(bits)
    return

if __name__ == '__main__':
    c = separateBits()
    # epsilion = epsilonNum(c)
    gamma = gammaNum(c)