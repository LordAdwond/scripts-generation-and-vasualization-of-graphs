import numpy as np
import os
import shutil

from random import randint, choice

# needed functions
def hasnt_zero_rows(A):
    for row in A:
        if sum(row)==0:
            return False
    return True

def is_good(A, n, l, L):
    M = [[0 for j in range(n)] for i in range(n)]
    M = [[1 if A[i][j]>0 else 0 for j in range(n)] for i in range(1, n)]

    check1 = np.sum(M) >= 2*(n-1)
    check2 = (sum([sum(row) for row in M])>=l) and (sum([sum(row) for row in M])<=L)
    check3 = hasnt_zero_rows(A)

    return check1 and check2 and check3

def into_txt(A : list[list], filepath : str):
    text = ""
    line = ""
    for row in A:
        line = ""
        for v in row:
            line = f"{line} {v} "
        text = text + line + '\n'
    with open(filepath, "w") as file:
        file.write(text)

# entering of needed parameters
N = int(input("Enter a number of graphs: "))
n = int(input("Enter a number of vertices: "))
l = int(input("Enter min number of edges: "))
L = int(input("Enter max number of edges: "))
min_w = int(input("Enter min weight of edge (must be natural): "))
max_w = int(input("Enter max weight of edge (must be natural): "))
num = 1

# checking of existence of directory "matrices"
if not os.path.exists("matrices"):
    os.mkdir("matrices")

# cleaning of directory "matrices"
folder_path = "matrices"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)  # delete files
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # delete directories
    except Exception as e:
        print(f'Error in time of dropping {file_path}. Reason: {e}')

# geterating of matrices and its writing into .txt files
while num<=N:
    A = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            u = randint(0, 1)
            oriented_to = choice([-1, 1])
            if u==1:
                if oriented_to==1:
                    A[i][j] = randint(min_w, max_w)
                elif oriented_to==-1:
                    A[j][i] = randint(min_w, max_w)

    if is_good(A, n, l, L):
        into_txt(A, f"matrices/{num}.txt")
        num += 1
    else:
        continue

print("Matrices is generated and written into path 'matrices' as txt files")
input()
