import fileinput
import re
from collections import defaultdict

def parseData():
    claim_list = []
    claim_data = {}
    i = 1
    for line in fileinput.input("day3input.txt"):

        result = re.findall("\d*", str(line))

        claim_list.append(result)



    claim_list_good = []
    for i in range(len(claim_list)):
        claim_copier = list(filter(lambda s: s != '', claim_list[i]))
        claim_list_good.append(claim_copier)


    return claim_list_good



def day3part1():

    claim_data = parseData()
    claims = {}
    claims = defaultdict(lambda: 0, claims)
    square_inches = 0

    for i in range(len(claim_data)):
            for col in range(1, int(claim_data[i][3])+1):
                for row in range(1, int(claim_data[i][4])+1):
                    updated_col = col + int(claim_data[i][1])
                    updated_row = row + int(claim_data[i][2])
                    claims[str(updated_row) + "_" + str(updated_col)] += 1


    print(claims)




    for i in claims.keys():

        if claims[i] < 2:
            continue
        else:
            square_inches += 1


    return square_inches




def day3part2():

        claim_data = parseData()
        claims = {}
        claims = defaultdict(lambda: [0], claims)
        square_inches = 0


        for i in range(len(claim_data)):
                for col in range(1, int(claim_data[i][3])+1):
                    for row in range(1, int(claim_data[i][4])+1):
                        updated_col = col + int(claim_data[i][1])
                        updated_row = row + int(claim_data[i][2])
                        claims[str(updated_row) + "_" + str(updated_col)][0] += 1
                        claims[str(updated_row) + "_" + str(updated_col)].append(i)
                        claims[str(updated_row) + "_" + str(updated_col)].append(int(claim_data[i][3])
                                                                                 *int(claim_data[i][4]))
        data_list = []
        one_claim = []
        for i in claims.keys():
            data_list.append(claims[i])


        expected_data = {}
        expected_data = defaultdict(lambda: 0, expected_data)

        made_data = {}
        made_data = defaultdict(lambda: 0, made_data)
        for i in range(len(data_list)):
            if data_list[i][0] != 1:
                continue
            else:
                expected_data[data_list[i][1]+1] += 1


        for i in range(len(claim_data)):
            value = int(claim_data[i][3])*int(claim_data[i][4])
            made_data[i+1] = value

        for j in made_data.keys():

            if made_data[j] == expected_data[j]:
                return j
























print(day3part2())





