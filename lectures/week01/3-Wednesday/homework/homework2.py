# Calculate a resturant tip based on 
# service and split between mutliple parties

tip = 0.0  #Variables

bill_total = 0.0

total_after_split = 0.0

bill_original = float(input("Total bill amount?"))

service_level = input("Level of service?")

split_amount = int(input("Split how many ways?"))

 #Checks input for level of service and makes calculations accordingly, then prints the solution
 
if service_level == "bad":
    tip = (bill_original * 0.10)

elif service_level == "fair":
    tip = (bill_original * 0.15)

elif service_level == "good":
    tip = (bill_original * 0.20)
    
    bill_total = tip + bill_original
    total_after_split =  (tip + bill_original) / split_amount 
    print("Tip amount = %.2f" % tip) 
    print("Total amount = %.2f" % bill_total)
    print("Amount per person = %.2f" % total_after_split)
