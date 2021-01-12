a = int(input("Значение А: "))
b = int(input("Значение B: "))
c = int(input("Значение С: "))

while a < b:
    print("Значение", a, "Пока что нет")
    a = a + c
if a > b:
    print("Дождались", a)