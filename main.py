import random

user_choise=0
user_score=0
door=5
ghost=0
print("           ...правила!...")
print("Вам потрібно вгадати дверь у якій немає привида, якщо ви натрапляєте на привида то ви програєте. За кожну вгадану дверь вам дається 1 бал, у кінці гри буде показано ваші бали")

while True:
#виводити наші двері
  for i in range(door):
    print("____["+str(i+1)+"]____")
#обираємо двері для привида
  ghost=random.randint(1,door)
#користувач обирає двері
  user_choise=int(input("Введіть номер дверей: "))
#виводимо відкриті двері
  for i in range(1,door+1):
    if i != ghost:
      print("[ ]")
    else:
      print("[G]")
#перевіряємо чи був привид за дверимв
  if user_choise==ghost:
    print("ВИ ПРОГРАЛИ!")
    break
  else:
    user_score=user_score+1
    print("--НОВИЙ РАУНД!--")

print("-----------------------")
print("Ви заробили "+str(user_score)+" балів")