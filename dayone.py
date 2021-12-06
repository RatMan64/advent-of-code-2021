#this is day one of advent of code


def NumOfIncrease():
    File_object = open("input1.txt", "r")
    input = File_object.readlines()
    File_object.close()
    numofincrease = 0
    prevousnum = 0
    firsttime = True

    for depth in range(len(input)):
        if firsttime == True:
            i = input[depth]
            firsttime = False
            prevousnum = int(i[:len(i)-1])
            continue
        num = input[depth]
        num = int(num[:len(num)-1])
        if prevousnum < num:
            numofincrease += 1
            prevousnum = num
            continue
        else:
            prevousnum = num
            continue
    print(numofincrease)
    return

def slidingwindow():
    File = open("input2.txt","r")



if __name__ == '__main__':
    slidingwindow()

