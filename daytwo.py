




def pos():
    file = open("inputdaytwo1.txt", "r")
    input = file.readlines()
    file.close()
    xpos=0
    ypos=0
    newinput = []
    for item in range(len(input)):
        newinput.append(input[item][:len(input[item])-1])


    print(newinput)


if __name__ == '__main__':
    pos()