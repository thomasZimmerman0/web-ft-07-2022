width = int(input("Width? "))

height = int(input("Height? "))

count = 2

print('*' * width)

while count < height:
    print('*' + (' ' * (width - 2)) + '*' )
    count += 1 

print('*' * width)
