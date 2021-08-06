T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input()) - 1

    div = 1
    div_upper = 1
    if n == 0:
        print(1)
    else:
        for i in range(1, k + 2):
            div *= i
        for j in range(1, k + 2):
            div_upper = div_upper * (n + j)

        print(int(div_upper / div))