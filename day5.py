from collections import defaultdict
import time

def day5part1():
    with open("day5demoinput.txt","r") as day5input:
        s = list(day5input.read())
    running = True

    while running:
        indices_to_remove = []
        for i in range(0, len(s)-1):
            if reaction(s, i, i+1):
                if (i not in indices_to_remove) and (i+1 not in indices_to_remove):
                    indices_to_remove.append(i)
                    indices_to_remove.append(i+1)


        if indices_to_remove:
            indices_to_remove.reverse()
            for i in indices_to_remove:
                del s[i]

        else:
            return len(s)

def day5part2():

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length_string = defaultdict(lambda: 0)
    for i in range(len(alphabet)):
        with open("day5input.txt", "r") as day5input:
            input_string = list(day5input.read())
        while alphabet[i] in input_string: input_string.remove(alphabet[i])
        while alphabet[i].upper() in input_string: input_string.remove(alphabet[i].upper())
        length_string[alphabet[i]] = react_string(input_string)
    return min(length_string.values())




def react_string(s):
    running = True
    while running:
        indices_to_remove = []
        for i in range(0, len(s)-1):
            if reaction(s, i, i+1):
                if (i not in indices_to_remove) and (i+1 not in indices_to_remove):
                    indices_to_remove.append(i)
                    indices_to_remove.append(i+1)



        if indices_to_remove:
            indices_to_remove.reverse()
            for i in indices_to_remove:
                del s[i]

        else:
            return len(s)

def reaction(s, index1, index2):
    if s[index1].lower() == s[index2].lower():
        if s[index1].isupper() and s[index2].islower() or s[index1].islower() and s[index2].isupper():
            return True
        else:
            return False

#start_time = time.time()
#print(day5part2())
print(day5part1())
