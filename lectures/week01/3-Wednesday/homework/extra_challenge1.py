first_100 = 100
dot_total = 1
bottom_quant = 1
new_row = 0
count = 0

while count < first_100:
    print(f"{dot_total}")
    new_row = bottom_quant + 1
    dot_total = dot_total + new_row
    bottom_quant = new_row
    count += 1
    
