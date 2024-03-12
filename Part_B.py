Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]


no_of_faces=6 # "no_of_faces" represents the number of sides or faces on the die
no_of_dies=2 # no_of_dies is the count of dies used  here
total_combinations=no_of_faces**no_of_dies  # eqn to find the total combination possible =no_of_faces^(no_of_dies)

sum_count = {}   #Sum_count={key= value}  here key is the sum  and value is the count , it is a dictionary to store the sum and count
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        s = Die_A[i] + Die_B[j]
        val = sum_count.get(s, 0) + 1    # sum_count.get retrieves the values associated with the sum  
        sum_count[s] = val         # 0 means presently there is no entries of that particular sum value
        
ref_prob = {key: val / total_combinations for key, val in sum_count.items()} # forming dict having sum and probablity

print(sum_count)
print("\nOriginal Probabilities:")
for key, val in ref_prob.items():
    print(f"Sum = {key}  count = {sum_count[key]}  Probability = {val:.2f}")
print("\n")

diceA=[]
diceB =[]

def dice_combos(number, temp, dice_list, limit):  # Returns all combinations for dice
    if number > limit:
        return
    if len(temp) > 6:
        return

    if len(temp) == 6:
        if temp not in dice_list:
            dice_list.append(temp)
        return

    for i in range(number, limit + 1):
        dice_combos(i, temp.copy() + [i], dice_list, limit)


def undoom_dice():

    diceA, diceB = [], []
    for i in range(1, 5):
        dice_combos(i, [i], diceA, 5)
        

    for j in range(1, 11):
        dice_combos(j, [j], diceB, 12) # since sum of 2 dices is never greater than 12
       
    print("First few combinations for Die A:")
    print(diceA[:5])

    print("\nFirst few combinations for Die B:")
    print(diceB[:5])
    print("After Undooming Dice A and Dice B")
    for i in diceA:
        for j in diceB:
            temp_dict = {}
            for k in range(len(i)):
                for l in range(len(j)):
                    s = i[k] + j[l]
                    val = temp_dict.get(s, 0) + 1
                    temp_dict[s] = val  #finding the sum for a particular combination

            match_count = sum(1 for key, val in temp_dict.items() if val == sum_count.get(key, -1))
            if match_count == 11:   # 11 distinct types of sums are there
                return i, j, temp_dict


New_Die_A, New_Die_B, temp_dict = undoom_dice()
print(f"New Dice A = {New_Die_A}")
print(f"New Dice B = {New_Die_B}")

