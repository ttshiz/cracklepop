# Python program to answer the CracklePop question

def main():
    for i in range(1, 101):
        if not i%3:
            if not i%5:
                print("Crackle Pop")
            else:
                print("Crackle")
        elif not i%5:
            print("Pop")
        else:
            print(i)
    return

if __name__ == "__main__":
    main()