import numpy as np

# Checks for 1-9 numbers present in file
def checkNumbers(file):
    for f in file:
        if type(f) not in [0,1,2,3,4,5,6,7,8,9]:
            return False
        else:
            return True

# Creates a sudoku puzzle out of a fileStream
def make_puzzle(fileStream):
    try:
        sudoku = np.array(fileStream)
        # Turn it into a sudoku grid
        sudoku.reshape(9,9)
        return sudoku
    except Exception as e:
        raise e

# Creates the 9 blocks within a sudoku puzzle
def slice_sudoku(sudoku, quad1, quad2, quad3, quad4 ,quad5, quad6, quad7, quad8, quad9):
    try:
        quad1 = sudoku[0:3, 0:3]
        quad2 = sudoku[0:3, 3:6]
        quad3 = sudoku[0:3, 6:8]
        quad4 = sudoku[3:6], 0:3]
        quad5 = sudoku[3:6, 3:6]
        quad6 = sudoku[3:6, 6:8]
        quad7 = sudoku[6:8], 0:3]
        quad8 = sudoku[6:8, 3:6]
        quad9 = sudoku[6:8, 6:8]
    except Exception as e:
        raise e
    return True

# Generates the global possibilities based on puzzle
def generate_possibilities(sudoku):
    possibilities = np.array([1,2,3,4,5,6,7,8,9]*81, shape=(9,9,9))
    possibilities


# Check quad
def checkQuad(quad):
    possibilities = [1,2,3,4,5,6,7,8,9]
    for a in possibilities:
        if x in quad:
            possibilities.pop(x)



# Checks the row in sudoku for any occurance of the particular number
def checkRow(sudoku, slice, row, num):



