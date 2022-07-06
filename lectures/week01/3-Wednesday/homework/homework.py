tip = 0.0

bill_total = 0.0

bill_original = input("What is the bill amount?")
bill_original = float(bill_original)

service_level = input ("How was the service?")


if service_level == "bad":
    bill_total = (bill_original * 0.10) + bill_original
    print(f"{bill_total}")
elif service_level == "fair":
    