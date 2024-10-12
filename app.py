a=[]
b=[]
count1=0
count2=0
while True:
  p1=int(input("Player 1: "))
  while p1<=0 or p1>9:
    print("Invalid input. Enter again.")
    p1=int(input("Player 1: "))
  while p1 in a or p1 in b:
    print("Cannot enter a number that is already taken. Enter again.")
    p1=int(input("Player 1: "))
    a.append(p1)
  if (1<=p1<=9) and p1 not in a:
    a.append(p1)

  for i in a:
    count1+=1
  print(count1)
  if set([1,2,3]).issubset(set(a)) or set([1,4,7]).issubset(set(a)) or set([7,8,9]).issubset(set(a)) or set([3,6,9]).issubset(set(a)) or set([1,5,9]).issubset(set(a))  or set([3,5,7]).issubset(set(a)) or set([4,5,6]).issubset(set(a)) or set([2,5,8]).issubset(set(a)):
    print("Player 1 wins")
    break

  elif count1+count2==9:
    print("It's a tie")
    break
  p2=int(input("Player 2: "))
  while p2<=0 or p2>9:
    print("Invalid input. Enter again.")
    p2=int(input("Player 2: "))
  while p2 in a or p2 in b:
    print("Cannot enter a number that is already taken. Enter again.")
    p2=int(input("Player 2: "))
  if (1<=p2<=9) and p2 not in b:
    b.append(p2)
  for i in b:
    count2+=1
  print(count2)
  if set([1,2,3]).issubset(set(b)) or set([1,4,7]).issubset(set(b)) or set([7,8,9]).issubset(set(b)) or set([3,6,9]).issubset(set(b)) or set([1,5,9]).issubset(set(b))  or set([3,5,7]).issubset(set(b)) or set([4,5,6]).issubset(set(b)) or set([2,5,8]).issubset(set(b)):
    print("Player 2 wins")
    break
