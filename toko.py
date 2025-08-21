item1 ={"nama" : "Odol",
           "stok": 10,
           "harga": 15000 }

item2 ={"nama" : "Keripik",
           "stok" : 10,
           "harga": 20000}

item3 ={"nama" : "Soda",
           "stok" : 15,
           "harga": 22000}

item4 ={"nama" : "Bumbu",
           "stok" : 15,
           "harga": 24000}

item5 ={"nama" : "Gula",
           "stok" : 20,
           "harga": 30000}

items = [item1, item2, item3, item4, item5]
for i in range(len(items)):
   print("item ke", i+1, "=", items[i]["nama"], items[i]["stok"], items[i]["harga"])
   
nama = str(input())
stok = str(input())
harga = str(input())

#crud add
item6 = {"nama":nama, "stok":stok, "harga":harga}
items.append(item6)
for j in range(len(items)):
   print("item ke", j+1, "=", items[j]["nama"], items[j]["stok"], items[j]["harga"])