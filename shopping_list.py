total = 0

products = ["répa", "retek", "mogyoró", "alma", "körte"]
prices = {"répa": 45, "retek": 50, "mogyoró": 55, "alma": 60, "körte": 65}

for elements in products:
    total += prices[elements]
print("Total: ", str(total))
