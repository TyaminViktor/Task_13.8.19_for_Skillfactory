A, Money, discount = int(input("Введите количество персон \n")), 0, 1
while A < 1:
    print("Введено неверное значение, попробуйте снова")
    A = int(input("Введите количество персон \n"))
Person_list = [int(input(f"Введите возраст персоны {B} - ")) for B in range(1, A+1)]
for i in Person_list:
    if i < 18:
        ticket = 0
    elif i < 25:
        ticket = 990
    else:
        ticket = 1390
    Money = Money + ticket
discount = 0.9 if len(Person_list) > 3 else 1
print(f"Цена посещения конференции - {Money * discount} руб.")
