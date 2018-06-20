def errorh(usinput):
    print("Welcome please enter and int!")
    while True:
        try:
            usinput = int(input(" "))
            print(usinput)
            if 0 / usinput == 0:
                print(">>>You entered the int: <<<{}>>> Good job!! Bye bye<<<".format(usinput))
                break

        except ValueError:
            print("That's not an int! try again...")


errorh(3)
