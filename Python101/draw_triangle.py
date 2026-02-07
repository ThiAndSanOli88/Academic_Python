""" 
This program draws a right justified triangle of 
asterisks based on the number of rows specified by the user.
For example, if the user enters 5, the output will be:
    *
   **
  ***
 ****
"""
def drawRightJustifiedTriangle(rows, columns):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()

def main():
    rows = int(input("How many lines do you want in your Asterisk Triangle?: "))
    drawRightJustifiedTriangle(rows, rows)
    
if __name__ == "__main__":
    main()