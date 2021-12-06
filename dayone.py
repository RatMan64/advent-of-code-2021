#this is day one of advent of code


def NumOfIncrease(input):


    numofincrease = 0
    prevousnum = 0
    firsttime = True

    for depth in range(len(input)):
        if firsttime == True:
            i = input[depth]
            firsttime = False
            prevousnum = i
            continue
        num = input[depth]

        if prevousnum < num:
            numofincrease += 1
            prevousnum = num
            continue
        else:
            prevousnum = num
            continue
    print(numofincrease)
    return



def sum(input):
    sum = 0

    for item in range(len(input)):
        sum += input[item]

    return sum



def slidingwindow():
    File = open("input2.txt","r")
    input = File.readlines()
    File.close()
    newinput = []
    for item in range(len(input)):
        a = input[item]
        b = int(a[:len(a)-1])
        newinput.append(b)

    count = 0
    c = []
    for item in range(len(newinput)):

        compare =(len(newinput) - 1) - item
        if 3 <= compare :
            segment = newinput[item: item+3]
            print(sum(segment))
            c.append(sum(segment))
            continue
        else:
            print(newinput[len(newinput)-3:])
            break
    print(NumOfIncrease(c))




if __name__ == '__main__':
    slidingwindow()

