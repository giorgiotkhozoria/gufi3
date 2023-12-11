list =["Andria Abuladze","Brian Taylor","Dachi Sazandrishvili","Dato Gafrindashvili","Gio Gagnidze","Giorgi Giorgi","Giorgi Jokhadze","Ioane Sarishvili","Jeko Tarieladze","Kosta Kostanyan","Leqso Leverashvili","Luka Sichinava","Mate Porchkhidze","Nika Koclamazashvili","Nikoloz Nutsubidze","Nodo Cinadze","Sandro Jalagonia","Yifiani Giga","Zaza Borisovi"]
print(list[6])



print("magaria" * 5)


b =list[1]
for i in list:
    if len(b) < len(i):
        b = i

g = list[1]
for i in list:
    if len(g) <len(i):
        g = i
    if i == b: g = g

print(b, g)