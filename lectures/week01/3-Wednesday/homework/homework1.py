tip = 0.0

bill_total = 0.0

bill_original = float(input("Total bill amount?"))
service_level = input("Levle of service?")

              
if service_level == "bad":
    tip = (bill_original * 0.10)
elif service_level == "fair":
    tip = (bill_original * 0.15)
elif service_level == "good":
    tip = (bill_original * 0.20)

else:
    print("Try entering good, bad, or fair")
    
bill_total =  tip + bill_original
print("Tip = %.2f" % tip) 
print("Bill Total = %.2f" % bill_total)
