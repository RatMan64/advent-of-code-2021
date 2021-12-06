
def decNum(input):


    return

def sanitize(input):
    newinput = []
    for item in range(len(input)):
        newinput.append(input[item][:len(input[item])-1])
    return newinput


def gammaNum(input):

    num = ""


    for item in range(len(input)):
        one = 0
        zero = 0
        segment = input[item]
        newsegment = segment[0]
        for bit in range(len(newsegment)):

            if newsegment[bit] == '0':
                zero += 1
            else:
                one +=1
        # print(zero)
        # print(one)
        if one > zero:
            num += "1"
        else:
            num += "0"
    return num

def epsilonNum(input ):

    num = ""

    for item in range(len(input)):
        one = 0
        zero = 0
        segment = input[item]
        newsegment = segment[0]
        for bit in range(len(newsegment)):

            if newsegment[bit] == '0':
                zero += 1
            else:
                one += 1
        # print(zero)
        # print(one)
        if one < zero:
            num += "1"
        else:
            num += "0"
    return num

def separateBits():
    file = open("inputdaythree1.txt", "r")
    input = file.readlines()
    file.close()
    newinput = sanitize(input)
    bits = [[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""],[""]]
    for row in range(len(newinput)):
        for bit in range(len(newinput[row])):
            bits[bit][0] += newinput[row][bit]


    return bits

if __name__ == '__main__':
    c = separateBits()
    epsilion = epsilonNum(c)
    print("epsilion is : " + epsilion)
    gamma = gammaNum(c)
    print("gamman is: "+ gamma)