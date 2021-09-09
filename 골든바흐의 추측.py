while(True):
  n = int(input())

  if n == 0:
    break

  a = [k for k in range(3, n)]
  b = []
  for i in a:
    for j in range(2,i):
      if i % j == 0:
        b.append(i)
  c = list(set(a)-set(b))
  c.sort()
  print("c : ", c)
  d = [n-k for k in c]
  print("d : ", d)
  e = [m for m in c if m in d]
  print("e : ", e)

  print("{0} = {1} + {2}".format(n, e[0], e[-1]))