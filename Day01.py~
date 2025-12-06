dial_position = 50
number_zeros = 0;

with open("Combos.txt", "r") as f:
    for line in f:
        # L or R
        direction = line[0] # STRING

        # % 100 gives one rotation distance
        value = int(line[1:]) % 100         
        
        # 100 needed as offset for 0
        if direction == "L":
            if value <= dial_position:
                dial_position -= value
            else:
                dial_position = 100 - (value - dial_position)
        else:
            if value <= (99 - dial_position):
                dial_position += value
            else:
                dial_position = value - (100 - dial_position)

        if (int(dial_position) == 0):
            number_zeros += 1;
        

print("Number Zeros: ", number_zeros)




        


