import csv
import math

def task(csv_string: str) -> float:
    reader = csv.reader(csv_string.strip().splitlines())
    matrix = [[int(value) for value in row] for row in reader]

    n = len(matrix)
    k = len(matrix[0])
    entropy = 0.0
    
    for j in range(k):
        for i in range(n):
            lij = matrix[i][j]
            if lij > 0:
                probability = lij / (n - 1)
                entropy -= probability * math.log2(probability)

    return round(entropy, 1)

if __name__ == "__main__":

    csv_string = """2,0,2,0,0
    0,1,0,0,1
    2,1,0,0,1
    0,1,0,1,1
    0,1,0,1,1"""

    result = task(csv_string)
    print(result)
