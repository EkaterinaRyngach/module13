n=int(input("Введите количество человек"))
price=0
price1=0
price2=990
price3=1390
discount=10
for i in range(n):
    age=int(input("Введите возраст %d посетителя"%(i)))
    if age<18:
        price+=price1
    elif age<25:
        price+=price2
    else:
        price+=price3
if n>3:
    price=int(price*((100-discount)/100))
print("Сумма= %d руб"%price)


