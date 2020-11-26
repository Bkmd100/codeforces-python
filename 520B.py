import sys
import threading
threading.stack_size(0x2000000)

sys.setrecursionlimit(12000)
output = 50000
seen, wanted = [int(x) for x in input().split()]

done_values = []
solutions = []


def cnn(n):
    global output
    output = min(n, output)




def fucker(n, r):
    global output
    if r >= 5010 or r>=output:
        return
    found = False
    for p in done_values:

        if n == p[0]:
            found = True
            if r >= p[1]:
                return
            else:
                p[1] = r
            break

    if not found:
        done_values.append([n, r])
    if n >= wanted:
        output = min(r + n - wanted, output)

    else:

        if n > 1:
           fucker(n - 1, r + 1)
        if n<= wanted/2+1:
            fucker(n * 2, r + 1)

threading.Thread(target=fucker(seen,0)).start()
while threading.activeCount()>1:
    pass
# print(solutions)
print(output)
# print(done_values)
#	print(done_values)
#
