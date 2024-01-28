################################################
# ******* triangle pattern *****************
################################################
N = 6
for i in range(0, N):
    for j in range(0, i):
        print("* ", end="")
    print()
for i in range(N, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print()

print("#"*50)
#####################################
# ***  diamond pattern ***** ######
#####################################

k = N-1
for i in range(0, N):
    for j in range(0, k):
        print(end=" ")
    k = k-1
    for j in range(0, i+1):
        print("* ", end="")
    print()

k = 1
for i in range(N, 0, -1):
    for j in range(0, k):
        print(end=" ")
    k = k+1
    for j in range(0, i-1):
        print("* ", end="")
    print()
