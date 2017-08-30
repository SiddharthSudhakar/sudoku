import numpy as np
import os
import csv
from sudoku_class import

# Loads a csv file with the sudoku puzzle
def load_sudoku(file, fileName, fileType='csv', delimit=' '):
    ext = '.' + fileType
    # Check for complete fileName
    if ext not in fileName:
        fileName = fileName + ext
    # For all csv files
    if fileType == 'csv':
        with open(filename, newline='') as csvfile:
            sudokuFile = csv.reader(csvfile, delimiter= delimit)
            if not checkNumbers(sudokuFile):
                print('Error: File is not in recognized sudoku type')
                return False
            else:
                return make_puzzle(sudokuFile)
    else:
        raise 'This type is not recognized!' + fileType
        return False


if __name__ == __main__:
    try:
        fileName = input('Enter the directory of the question sudoku file')
        fileType = input('Enter file Type (eg. csv, xlsx, etc.)')
        delimit = input('Enter delimiter in the file (eg. "," , "|" , etc. )')
    except IOError:
        raise IOError
    except Exception as e:
        raise e
    # Load Puzzlefile
    sudokuPuzzle = load_sudoku(file, fileName, fileType)
    if sudokuPuzzle is False:
        raise 'Unidentified Error! Halting program'
        exit()
    else:
        # Solve Puzzle file
        sudoku_solver(sudokuPuzzle)