def kettovel_szorozz(x):
    while True:
        x = int(input("Adj egy számot! "))
        if x < 0:
            raise ValueError("Sorry, no numbers below zero")
        else:
            x = x * 2
            return x


def main(x):
    try:
        y = (kettovel_szorozz(x)) * 3
        print(y)
        print(x)
    except ValueError as sorry:
        print(sorry)
        print("bejöttem az excepthez")

    print("tovább mentem")
    print("itt a vége")


main(5)
