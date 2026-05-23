def main():
    print("Meow Meow")

    meow()
    cat()


def meow():
    i = 3

    while i != 0:
        print("meow")

        i = i - 1


def cat():
    animal = input("What animal do you want? ")

    if animal == "cat":
        print("mew mew")


main()
