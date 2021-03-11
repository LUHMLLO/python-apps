print("")
print("Digite una cantidad a retirar")

dinero = int(input("Cantidad : "))


billete_de_2000= dinero // 2000; billete_de_2000i = dinero % 2000
billete_de_1000= billete_de_2000i // 1000; billete_de_1000i = dinero % 1000
billete_de_500= billete_de_1000i // 500; b500i = dinero % 500
billete_de_200= b500i // 200; billete_de_200i = b500i % 200
billete_de_200= billete_de_200i // 100; billete_de_100i = billete_de_200i % 100
billete_de_50= billete_de_100i // 50; b50i = billete_de_100i % 50

billete_de_25= b50i // 25; billete_de_25i = b50i % 25
billete_de_10= billete_de_25i // 10; billete_de_10i = billete_de_25i % 10
billete_de_5= billete_de_10i // 5; b5i = billete_de_10i % 5
billete_de_1 = b5i // 1; billete_de_1i = b5i % 1


if billete_de_2000 >= 1:
    print(str(billete_de_2000) + " billete" +('s' if (billete_de_2000) > 1 else '') + " de 2000")
if billete_de_1000 >= 1:
    print(str(billete_de_1000) + " billete" +('s' if (billete_de_1000) > 1 else '') + " de 1000")
if billete_de_500 >= 1:
    print(str(billete_de_500) + " billete" +('s' if (billete_de_500) > 1 else '') + " de 500")
if billete_de_200 >= 1:
    print(str(billete_de_200) + " billete" +('s' if (billete_de_200) > 1 else '') + " de 200")
if billete_de_200 >= 1:
    print(str(billete_de_200) + " billete" +('s' if (billete_de_200) > 1 else '') + " de 100")
if billete_de_50 >= 1:
    print(str(billete_de_50) + " billete" +('s' if (billete_de_50) > 1 else '') + " de 50")
if billete_de_25 >= 1:
    print(str(billete_de_25) + " moneda" +('s' if (billete_de_25) > 1 else '') + " de 25")
if billete_de_10 >= 1:
    print(str(billete_de_10) + " moneda" +('s' if (billete_de_10) > 1 else '') + " de 10")
if billete_de_5 >= 1:
    print(str(billete_de_5) + " moneda" +('s' if (billete_de_5) > 1 else '') + " de 5")
if billete_de_1 >= 1:
    print(str(billete_de_1) + " moneda" +('s' if (billete_de_1) > 1 else '') + " de 1")
