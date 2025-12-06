dialPosition = 50
numberZeros = 0

x = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

iters = 0
with open("Combos.txt", "r") as f:
    for line in f:
    #for line in x:
        # L or R
        direction = line[0] # STRING
        value = int(line.strip()[1:])

        # % 100 gives one rotation distance
        if value >= 100:
            numberZeros += value // 100
            value %= 100
        
        if direction == "L":
            if value == dialPosition:
                dialPosition = 0
                numberZeros += 1

            elif value > dialPosition:
                if not dialPosition == 0:
                    numberZeros += 1
                value = value - dialPosition
                dialPosition = 100 - value

            else:
                dialPosition -= value
        else:
            if value == (100 - dialPosition):
                numberZeros += 1
                dialPosition = 0

            elif value > (100 - dialPosition):
                numberZeros += 1
                dialPosition = (value - (100 - dialPosition))

            else: 
                dialPosition += value


print("Number Zeros: ", numberZeros)
