for _ in range(int(input())):
  b = bin(int(input()))[2:][::-1]

  print(*[i for i in range(len(b)) if b[i] == '1'])

