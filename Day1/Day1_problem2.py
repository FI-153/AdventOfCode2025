start_pos = 50
num_elems = 100

safe = [i for i in range(num_elems)]
index = start_pos
password = 0

with open('input.txt', 'r') as file:
    for line in file:

        amount = int(line[1:])
        mvmnt = 1 if line[0] == "R" else -1

        for _ in range(0, amount):

            if index == 0 and mvmnt == -1:
                index = 99
            else :
                index = (index + mvmnt) % num_elems

            if index == 0:
                password+=1

print(password)