dialPosition = 50 

numberZeros = 0;

with open("Combos.txt", "r") as f:
    for line in f:

        # L or R
        direction = line[0] # STRING

        value = int(line[1:])

        if (int(dialPosition) == 0):
            numberZeros += 1;

        if value > 100:
            numberZeros += int(value / 100)
            value %= 100

        if direction == "L":
            if value <= dialPosition:
                dialPosition -= value
            else:
                if (int(dialPosition) != 0 and 100 - (value - dialPosition) != 0):
                    numberZeros += 1;
                dialPosition = 100 - (value - dialPosition)
        else:
            if value <= (100 - dialPosition):
                dialPosition += value
            else:
                if (int(dialPosition) != 0 and value - (100 - dialPosition) != 0):
                    numberZeros += 1;
                dialPosition = value - (100 - dialPosition)

        

print("Number Zeros: ", numberZeros)




        


