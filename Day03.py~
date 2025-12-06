invalid_ids = 0

id_range_list = []

with open('IdRanges.txt', 'r') as f:
    id_range_list = f.read().split(",")
    
for id_range in id_range_list:
    start = int(id_range[:id_range.find('-')])
    end = int(id_range[1 + id_range.find('-'):])

    for value in range(start, end+1):
        value = str(value)

        num1 = value[:len(value) >> 1]
        num2 = value[len(value) >> 1:]

        if num1 == num2:
            invalid_ids += int(value)
   

print(f'Invalid Ids total value: {invalid_ids}')

