initial = ["Dog","Dog","Dog", "Cat", "Mouse", "Hat"]
remove_dup = []


for i in initial:
    if i not in remove_dup:
        remove_dup.append(i)

print(remove_dup)
