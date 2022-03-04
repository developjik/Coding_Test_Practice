from sys import stdin
input = stdin.readline

n = int(input())
card = list((map(int, input().split())))
gold = 0

if n == 1:
  print(gold)
else: 
  while len(card) != 1:
    max_index = card.index(max(card))

    if max_index - 1 == -1:
      gold += card[0] + card[1]
      card.pop(1)
    elif max_index + 1 == len(card):
      gold += card[len(card)-1] + card[len(card)-2]
      card.pop(len(card)-2)
    else: 
      if card[max_index-1] >= card[max_index+1]:
        gold += card[max_index] + card[max_index-1]
        card.pop(max_index-1)
      else:
        gold += card[max_index] + card[max_index+1]
        card.pop(max_index+1)

print(gold)