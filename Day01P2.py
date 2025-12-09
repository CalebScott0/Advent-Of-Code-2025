dial_position = 50
number_zeros = 0

with open("Combos.txt", "r") as f:
    for line in f:
    #for line in x:
        # L or R
        direction = line[0] # STRING
        value = int(line.strip()[1:])

        # % 100 gives one rotation distance
        if value >= 100:
            number_zeros += value // 100
            value %= 100
        
        if direction == "L":
            if value == dial_position:
                dial_position = 0
                number_zeros += 1

            elif value > dial_position:
                if not dial_position == 0:
                    number_zeros += 1
                value = value - dial_position
                dial_position = 100 - value

            else:
                dial_position -= value
        else:
            if value == (100 - dial_position):
                number_zeros += 1
                dial_position = 0

            elif value > (100 - dial_position):
                number_zeros += 1
                dial_position = (value - (100 - dial_position))

            else: 
                dial_position += value


print("Number Zeros: ", number_zeros)
