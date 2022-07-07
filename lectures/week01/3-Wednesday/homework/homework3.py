coin_quant = 0
says_yes= "yes"

while says_yes == "yes" and says_yes != "no" :
    print(f"you have {coin_quant} coins.")
    says_yes = input("Do you want another coin? ")
    if says_yes == "yes":
        coin_quant += 1
print("Bye")