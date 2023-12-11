b = ""
cap_sia = []
supersia = []
list =["Andria Abuladze","Brian Taylor","Dachi Sazandrishvili","Dato Gafrindashvili","Gio Gagnidze","Giorgi Giorgi","Giorgi Jokhadze","Ioane Sarishvili","Jeko Tarieladze","Kosta Kostanyan","Leqso Leverashvili","Luka Sichinava","Mate Porchkhidze","Nika Koclamazashvili","Nikoloz Nutsubidze","Nodo Cinadze","Sandro Jalagonia","Yifiani Giga","Zaza Borisovi"]
for i in list:
    if i.count('o') == 2:
        supersia.append(i)

print(supersia)




for i in list:
    if len(i) > 16:
       b = i.upper()
    cap_sia.append(b)
    
print(cap_sia)