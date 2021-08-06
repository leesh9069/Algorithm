N = int(input())

quotient = []
for i in range(2, N+1):
  if N%i == 0:
    quotient.append(i)

for j in quotient:
  while N % j == 0:
    N = N / j
    print(j)