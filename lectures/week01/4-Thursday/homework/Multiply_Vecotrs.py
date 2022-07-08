set1 = [4 , 4 , 9]
set2 = [15, 3, 7]
solution = []

index = 0

while index < len(set1) :
    solution.append(set1[index] * set2[index])
    index += 1
print(solution)
    