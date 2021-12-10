import time

labels = {
    "main": None
}
variables = {
    "$version": "1.0",
    "count": 0
}

def executeLabel (name: str):
    for line in labels.get(name):
        variables["count"] = variables["count"] + 1

        if variables.get("count") == 150:
            print("I AM SO TIRED PLEASE STOP")
        if variables.get("count") > 150:
            if random.randrange(0, 10) == 0:
                print("This is so stressful OMG")
                continue
        if variables.get("count") == 250:
            print("I CANT DO THIS ANYMORE")
            exit(0)


        interpret(line)
        time.sleep(variables.get("count") * 0.003)


def interpret(line: list):
    if len(line) != 0 and line[0] != "{":
        if line[0] == '<<':
            print(getData(line, 1))
        if line[0] == '»':
            if line[1] == 'count':
                print("DONT TRY To MESS WITH ME")
                exit()

            if line[2] == '<-':
                variables[line[1]] = getData(line, 3)
            if line[2] == '++':
                variables[line[1]] = variables[line[1]] + 1
            if line[2] == '--':
                variables[line[1]] = variables[line[1]] - 1
        if line[0] == '=>':
            if len(line) == 2:
                executeLabel(line[1])
            elif line[2] == '->':
                if doIf(line, 3):
                    executeLabel(line[1])
        if line[0] == '?':
            exit(getData(line, 1))

def doIf(line, index):
    max = -1
    for i in range(index + 1, len(line)):
        if line[i] == '||':
            max = i + 1
            break
    if line[index] == '=':
        return getData(line, index + 1) == getData(line, max) 
    if line[index] == '<':
        return getData(line, index + 1) < getData(line, max) 
    if line[index] == '>':
        return getData(line, index + 1) > getData(line, max) 

def getData(line: list, index: int):
    if line[index] == '>>':
        return input()
    if line[index] == '>>>':
        return int(input())
    if line[index].startswith("→"):
        temp = ""
        for i in range(index + 1, len(line)):
            if line[i].endswith("←"):
                return temp
            else:
                temp+= line[i] + " "
    if variables.get(line[index]) is not None:
        return variables.get(line[index])
    try:
        return int(line[index])
    except:
        return float(line[index])




def analyze_labels (linesAsString: str):
    lbls = linesAsString.split("lbl ")
    for lbl in lbls:
        try:
            labels[lbl.split(" {")[0]] = convert(lbl.split(" {")[1].split("\n"))
        except:
            pass
    print(labels)

def convert(s_lines: list):
    lines = []
    for s in s_lines:
        temp = s.split(' ')
        temp2 = []
        f = True
        for word in temp:
            if word == '' and f:
                continue
            else:
                temp2.append(word)
                f = False
        lines.append(temp2)
    return lines

def shell():
    running = True
    while running:
        interpret(input(":: ").split(" "))

if __name__ == '__main__':
    import random
    if (random.randrange(0, 3) == 0):
        print("NO!!!")
        exit(0)
    print("Interpreter is starting")
    f = open("./config.bsc").read()
    if (f.split("\n")[1] == 'true'):
        shell()
    file = open(f.split("\n")[0])
    analyze_labels(file.read())
    executeLabel("main")