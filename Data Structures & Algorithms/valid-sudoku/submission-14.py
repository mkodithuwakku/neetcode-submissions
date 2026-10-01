class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row, column, and sub box needs a set
        # Check if each column is valid
        # Iterate through the column and add new elements to the set
        # If element exists in the set, the column is invalid and return false
        colSet = set()
        i = 0

        
        while i < 9:
            colSet = set()
            for arr in board:
                if arr[i] not in colSet:
                    colSet.add(arr[i])
                
                elif arr[i] == ".":
                    continue
                else :
                    return False
                
            i = i + 1

        # Check if each row is valid
        # Iterate through the row and add new elements to the set
        # If element exists in the set, the row is invalid and return false

        for arr in board:
            rowSet = set()
            for elem in arr:
                if elem not in rowSet:
                    rowSet.add(elem)
                
                elif elem == ".":
                    continue
                else :
                    return False
        
        
        
       
        # Check if each sub-box is valid 
        squareSets = [set() for _ in range(9)] # NEW SYNTAX
        for row in range (9):
            rowIndex = row // 3
            for col in range(9):
                cell = board[row][col]
                colIndex = col // 3
                
                if cell == ".":
                    continue
                elif rowIndex == 0 and colIndex == 0:
                    if cell in squareSets[0]:
                        return False
                    else:
                        squareSets[0].add(cell)

                elif rowIndex == 0 and colIndex == 1:
                    if cell in squareSets[1]:
                        return False
                    else:
                        squareSets[1].add(cell)
                
                elif rowIndex == 0 and colIndex == 2:
                    if cell in squareSets[2]:
                        return False
                    else:
                        squareSets[2].add(cell)

                elif rowIndex == 1 and colIndex == 0:
                    if cell in squareSets[3]:
                        return False
                    else:
                        squareSets[3].add(cell)

                elif rowIndex == 1 and colIndex == 1:
                    if cell in squareSets[4]:
                        return False
                    else:
                        squareSets[4].add(cell)

                elif rowIndex == 1 and colIndex == 2:
                    if cell in squareSets[5]:
                        return False
                    else:
                        squareSets[5].add(cell)

                elif rowIndex == 2 and colIndex == 0:
                    if cell in squareSets[6]:
                        return False
                    else:
                        squareSets[6].add(cell)

                elif rowIndex == 2 and colIndex == 1:
                    if cell in squareSets[7]:
                        return False
                    else:
                        squareSets[7].add(cell)

                elif rowIndex == 2 and colIndex == 2:
                    if cell in squareSets[8]:
                        return False
                    else:
                        squareSets[8].add(cell)
            
        return True

                

                



