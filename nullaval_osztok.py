def valamivel_osztok(x,y):
    if x < 0:
        raise ValueError("Ne adj osztandónak mínusz számot")
    elif y==0:
        raise ZeroDivisionError("Ne adj osztónak nullát")
    else:
        z = x // y
        return z


def main():
    while True:
        try:
            x=int(input("Add meg az osztandót!: "))
            y=int(input("Add meg az osztót!: "))
            vegeredmeny = (valamivel_osztok(x,y)) + 100
            print("A kis függvény eredménye: ", valamivel_osztok(x,y))
            print("A Main függvény eredménye: ", vegeredmeny)
        except ValueError as err:
            print("Cakk")
            print(err)
        except ZeroDivisionError as zero:
            print("Cikk-cakk")
            print(zero)

        print("itt a vége")


main()