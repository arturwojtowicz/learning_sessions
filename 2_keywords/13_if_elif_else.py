# elif and else
print("----------- if, elif and else -----------")
for i in range(5):
    print("Start", i)
    if i == 0:
        continue
    elif i == 1:
        pass
    else:
        break
    print("End:", i)
