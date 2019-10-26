print("This program will make your text lowercase. Let's being!")

while True:
    text = input("Enter upper- and/or lowercase text: ")
    print(text.lower())

    end = input("Do you have more text? ")
    if end.lower() == "no":
        break
