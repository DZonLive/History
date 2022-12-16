def create2dArr(m, n):
    arr2d = []

    for i in range(m):
        arr2d.append([])
        for j in range(n):
            arr2d[i].append(0)

    return arr2d

def print_matrix(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j], end=" ")
        print()


a = create2dArr(9, 9)

print_matrix(a)

a = [[1, 2, 3, 5, 6], [4, 5, 6, 4, 3], [7, 8, 9, 5, 9]]
def mirror_2(a):
    for i in range(len(a)):
        for j in range(len(a[0]) - 1, -1, -1):
            print(a[i][j], end=' ')
        print()
