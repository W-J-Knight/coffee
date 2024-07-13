Mun_ITEMS = 5

#initalized list of add-ins.
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

addInPrices = [.89, .25, .59, 1.50, .175]

orderTotal = 2.00
addIn = 0
while addIn != "XXX":
    addIn = input("Enter coffee add-in of XXX to quit: ")
    if addIn in addIns:
        foundIt = True
        indexFoundIt = addIns.index(addIn)
        print(indexFoundIt)
        print(f"{addIn} Price is $ {addInPrices[indexFoundIt]}")
        orderTotal = orderTotal + addInPrices[indexFoundIt]
    else: print("Sorrry, we do not carry that.")

print(f"Order Total is ${format(orderTotal, ".2f")}")