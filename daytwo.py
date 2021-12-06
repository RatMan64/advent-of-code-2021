




def pos():
    file = open("inputdaytwo2.txt", "r")
    input = file.readlines()
    file.close()
    xpos=0
    ypos=0
    aim = 0
    newinput = []
    for item in range(len(input)):
        newinput.append(input[item][:len(input[item])-1])

    for item in range(len(newinput)):
        command = newinput[item].split(" ")
        if command[0] == "forward":
            ypos += aim *int(command[1])
            xpos += int(command[1])
            continue
        if command[0] == "up":
            aim -= int(command[1])
            continue
        if command[0] == "down":
            aim += int(command[1])
            continue

    print(xpos*ypos)



if __name__ == '__main__':
    pos()