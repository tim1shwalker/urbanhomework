def get_matrix(n, m, value):
    matrix = []


    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)


        matrix.append(row)


    return matrix
result1 = get_matrix(2,5,30)
result2 = get_matrix(2,7,1)
result3 = get_matrix(5,10,4)

print(result1)
print(result2)
print(result3)
