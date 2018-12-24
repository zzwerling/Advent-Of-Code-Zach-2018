import fileinput
import re
import operator
from collections import defaultdict
times = []

def sortData():
    for line in fileinput.input("day4input.txt"):
        time_list = []
        timedata = re.findall('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})', str(line))
        guarddata = re.findall('Guard #(\d*)', str(line))
        fallasleep = re.findall('falls asleep', str(line))
        wakesup = re.findall('wakes up', str(line))

        for i in timedata[0]:
            time_list.append(int(i))

        if len(guarddata) > 0:
            time_list.append(int(guarddata[0]))
        elif len(fallasleep) > 0:
            time_list.append(fallasleep[0])
        else:
            time_list.append(wakesup[0])

        times.append(time_list)

    times.sort()

    return times

def sort_and_write():
    with open("day4input.txt") as f:
        data = sorted(f.readlines())

    with open("day4testinput.txt", "w") as f:
        f.write("".join(data))


def day4part1():
    shift_data = sortData()
    wakeup_map = defaultdict(lambda: [])
    print(shift_data)

    for i in range(len(shift_data)-1):

        action = shift_data[i][5]

        if not isinstance(action, int):
            continue

        for j in range(i+1, len(shift_data)):

            hours = shift_data[j][3]
            minutes = shift_data[j][4]
            iterated_action = shift_data[j][5]



            if isinstance(iterated_action, int):
                break
            else:
                wakeup_map[action].append([hours, minutes])
                #wakeup_map[action].append(minutes)

    total_asleep = defaultdict(lambda: 0)
    for key in wakeup_map.keys():
        for i in range(0, len(wakeup_map[key])-1, 2):
            hour1 = wakeup_map[key][i][0]
            minute1 = wakeup_map[key][i][1]
            hour2 = wakeup_map[key][i+1][0]
            minute2 = wakeup_map[key][i+1][1]

            #print(hour1, minute1, hour2, minute2)

            total_asleep[key] += find_time_difference(hour1, minute1, hour2, minute2)

    #most_common_hour(wakeup_map[2351])
    most_common_hour_all(wakeup_map)


def most_common_hour_all(guard_map):

    nested_times = defaultdict(lambda: defaultdict(lambda: 0))

    for key in guard_map.keys():
            for i in range(0, len(guard_map[key]), 2):

                minute1 = guard_map[key][i][1]
                minute2 = guard_map[key][i+1][1]

                for j in range(minute1, minute2+1):
                    nested_times[key][j] += 1


    print(nested_times)
    max_values = defaultdict(lambda: 0)

    print(max([(x, y, nested_times[x][y]) for x in nested_times for y in nested_times[x] if x != y], key=lambda x: x[2]))


def most_common_hour(list):

    minutes_asleep = defaultdict(lambda: 0)

    for i in range(0, len(list), 2):
        minute1 = list[i][1]
        minute2 = list[i+1][1]

        for j in range(minute1, minute2+1):
            minutes_asleep[j] += 1

    print(max(minutes_asleep.items(), key=operator.itemgetter(1))[0])






















def find_time_difference(hour1, minute1, hour2, minute2):

    if hour1 == hour2:
        return minute2 - minute1

    else:
        return (60-minute1) + minute2

#print(sortData())
#print(sort_and_write())
print(day4part1())
#guard 1
#falls asleep
#wakes up
#guard 2




