




def pos():
    file = open("inputdaytwo1.txt", "r")
    input = file.readlines()
    file.close()
    xpos=0
    ypos=0
    newinput = []
    for item in range(len(input)):
        newinput.append(input[item][:len(input[item])-1])

    for item in range(len(newinput)):
        command = newinput[item].split(" ")
        if command[0] == "forward":
            xpos += int(command[1])
            continue
        if command[0] == "up":
            ypos -= int(command[1])
            continue
        if command[0] == "down":
            ypos += int(command[1])
            continue

    print(xpos*ypos)



if __name__ == '__main__':
    pos()