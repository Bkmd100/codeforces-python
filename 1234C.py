q = int(input())
j = 0
j1 = 0
final = []


def super():
    global j, j1
    l = int(input())
    x1 = input()
    y1 = input()
    x = [[int(xx) for xx in str(x1)], [int(xx) for xx in str(y1)]]
    global j
    for j in [0, 1]:
        for i in range(0, len(x[j])):
            if x[j][i] in [1, 2]:
                x[j][i] = 0
            else:
                x[j][i] = 1

    j = 0
    j1 = 0

    def next():

        global j, j1
        j1 = j
        if j == 0:
            j = 1
            return 1
        else:
            j = 0
            return 0

    flip = False
    i = 0
    while i < l - 1:

        if x[j][i] == 1:

            if not flip:
                flip = True

                if x[next()][i] != 1:
                    final.append("NO")
                    return

            else:
                flip = False
                i += 1
        else:

            i += 1

    if (j == 0 and x[0][l - 1] == 1 and x[1][l - 1] == 1 and not flip) or \
            (j == 1 and flip and x[1][l - 1] == 1 and j == j1) or (j == 1 and x[1][l - 1] == 0):
        final.append("YES")
    else:
        final.append("NO")


for i in range(0, q):
    super()

for t in final:
    print(t)
