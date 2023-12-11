import random
list =["Andria Abuladze","Brian Taylor","Dachi Sazandrishvili","Dato Gafrindashvili","Gio Gagnidze","Giorgi Giorgi","Giorgi Jokhadze","Ioane Sarishvili","Jeko Tarieladze","Kosta Kostanyan","Leqso Leverashvili","Luka Sichinava","Mate Porchkhidze","Nika Koclamazashvili","Nikoloz Nutsubidze","Nodo Cinadze","Sandro Jalagonia","Yifiani Giga","Zaza Borisovi"]
print(random.choice(list)," kargad swavlobs")
print(random.choice(list)," kargad swavlobs")
print(random.choice(list)," kargad swavlobs")

for i in list:
    if i.endswith("i"):
        print(i, "cool")