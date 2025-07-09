for i in range(1,3):
    for j in range(3,6):
        print ((i),(j))

for num in range (1,20,2):
    if num == 15:
        break
    print(num)

## WAP, Take user input for start, Stop and Skip numbers

start = int(input('enter start ='))
stop = int(input('enter stop ='))
skip = int(input('number you want to skip ='))
for i in range (start, stop):
    if i == skip:
        continue
    print(i)