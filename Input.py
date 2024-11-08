import numpy as np

def get_one_metrix():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    while True:
        try:
            cols = int(input("Enter the number of columns: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    while True:
        metrix = []
        for i in range(rows):
            while True:
                row = input(f"Enter row {i + 1} (space-separated values): ").split()
                if len(row) == cols:
                    try:
                        metrix.append([int(x) for x in row])
                        break
                    except ValueError:
                        print("Invalid input. Please enter integers only.")
                else:
                    print(f"Error: You must enter exactly {cols} elements.")
        
        metrix = np.array(metrix)
        print("You have entered the following matrix:")
        print_metrix(metrix)
        
        re_enter = input("Do you want to re-enter the matrix? (y to re-enter): ").strip().lower()
        if re_enter != 'y':
            break
    
    return metrix

def print_metrix(metrix):
    for row in metrix:
        print(f"[{' '.join(map(str, row))}]")

def get_two_metrix():
    while True:
        print("Enter the first metrix:")
        metrix1 = get_one_metrix()
        
        print("Enter the second metrix:")
        metrix2 = get_one_metrix()
        
        print("Metrix 1:")
        print_metrix(metrix1)
        print("Metrix 2:")
        print_metrix(metrix2)
        
        re_enter = input("Do you want to re-enter the matrices? (y to re-enter): ").strip().lower()
        if re_enter != 'y':
            break
    
    return metrix1, metrix2
