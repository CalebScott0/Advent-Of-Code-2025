dialPosition = 50
numberZeros = 0;

iters = 0;

with open("Combos.txt", "r") as f:
    for line in f:
        iters += 1
        # L or R
        direction = line[0] # STRING

        # % 100 gives one rotation distance
        value = int(line[1:]) % 100         
        
        # 100 needed as offset for 0
        if direction == "L":
            if value <= dialPosition:
                dialPosition -= value
            else:
                dialPosition = 100 - (value - dialPosition)
        else:
            if value <= (99 - dialPosition):
                dialPosition += value
            else:
                dialPosition = value - (100 - dialPosition)

        if (int(dialPosition) == 0):
            numberZeros += 1;
        

print("Number Zeros: ", numberZeros)




        


