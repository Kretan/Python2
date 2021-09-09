# check whether a number falls in a range

import webbrowser


def range_ben_van_e(x):
    x = int(input("Add meg a születési évszámodat!: "))
    if x in range(2003, 2022):
        return False
    elif x >= 2022:
        raise ValueError
    return True


def weboldal_nyitas():
    webbrowser.open("https://pythonexamples.org", new=1)

def main():
    while True:
        x = 0
        try:
            if range_ben_van_e(x):
                weboldal_nyitas()
                break
            else:
                print("Túl fiatal vagy, próbáld meg később")
        except ValueError:
            print("Rossz évszámot adtál meg, próbáld újra")


main()
