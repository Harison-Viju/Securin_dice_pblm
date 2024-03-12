# Problem Statement: The Doomed Dice Challenge
# The below problems must be solved & implemented in Python/Java/Ruby/C++/Go
# You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6.
# You can only roll both the dice together & your turn is guided by the obtained sum.
# Example: Die A = 6, Die B = 3. Sum = 6 + 3 = 9
# You may represent Dice as an Array or Array-like structure.
# Die A = [1, 2, 3, 4, 5, 6] where the indices represent the 6 faces of the die & the value on each face.

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# 1. How many total combinations are possible? Show the math along with the code!
no_of_faces=6 # "no_of_faces" represents the number of sides or faces on the die
no_of_dies=2 # no_of_dies is the count of dies used  here
total_combinations=no_of_faces**no_of_dies  # eqn to find the total combination possible =no_of_faces^(no_of_dies)
print("1 :Total Combinations possible:",total_combinations)


# 2. Calculate and display the distribution of all possible combinations that can be
# obtained when rolling both Die A and Die B together. Show the math along with
# the code!
# Hint: A 6 x 6 Matrix

n=no_of_faces
sum=[[0 for _ in range(n)] for _ in range(n) ]
def distribution(Die_A,Die_B):
    
    
    print("2 :Displaying the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together ")
    for i in Die_A:
        for j in Die_B:
            print("(",i,",",j,")", end="\t")
        print()

    print("Table showing the sum of numbers in the distribution:")
    for i in Die_A:
        for j in Die_B:
            sum[i-1][j-1]=i+j
            print(sum[i-1][j-1], end="\t")
        print()
    return(sum)

sum=distribution(Die_A,Die_B)
#3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).
# Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain
# Sum = 2. Die A = Die B = 1
probablity=[[0 for _ in range(n)] for _ in range(n)]
def prob(Die_A,Die_B):
    print("Probability of all Possible Sums occurring among the number of combinations")    
    
    for i in range(n):
        for j in range(n):
            count=0
            for x in range(n):
                for y in range(n):
                    if (sum[i][j]==sum[x][y]):
                        count+=1
            probablity[i][j]=count/total_combinations
            print(f"{probablity[i][j]:.2f}", end="\t")
        print()
prob(Die_A,Die_B)


