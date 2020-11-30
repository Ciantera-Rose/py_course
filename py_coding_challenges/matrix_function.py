
#Manually Build an Incrementing Matrix Function in Python
#Build a function that outputs exact values
#manual_increments_matrix(5)
#List that contains lists inside of it
#5 elements inside each list starting at the 0 index
#Autofill and incement
#Function needs to preform being able to output thhe exact values

array = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]

"""
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""
#Build a matrix. Starts with empty values
#Matrix n * n of size
#List comp: 


def manual_incrementing_matrix(n): #Pass in argument of n
    matrix = [ [ None for y in range(n) ] for x in range(n) ]

#List comprehension that allows a list with lists inside of it. 
#Build a set of empty values and define how many we want it to create for us
#Creates skeleton for the matrix
#Next need to populate it
#Incrememt count. Starts at 0 

    counter = 0
#Keeps track of a number
#Make a nested for loop
#For index, element... 
#Cast matrix to ennumerate function. Loop list 

    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el): 
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix

print(manual_incrementing_matrix(5))


def increment_matrix(grid_area):
    starting_num = 0
    initial_matrix = grid_area
    matrix = []

    while starting_num != initial_matrix:
        matrix.append(list(range(starting_num, grid_area)))
        starting_num += 1 
        grid_area += 1

        return matrix

    print(increment_matrix(5))

