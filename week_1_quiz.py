with open("currency.txt", "r") as file_object:
    doc = file_object.readlines()

for line in doc:
    line = line.split()

currency_list = [{} for i in range(len(doc))]

x = 0
for i in currency_list:
    i["symbol"] = doc[x][0:3]
    x += 1

x = 0
for i in currency_list:
    i["rate"] = doc[x][4:-2:1]
    x += 1

print(currency_list)
