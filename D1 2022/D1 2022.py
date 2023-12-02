def paaohjelma():
    Summa = 0
    Kalorit = []
    Tiedosto = open("D1.txt","r")
    Rivi = Tiedosto.readline()
    while len(Rivi) > 0:
        if Rivi == "\n":
            Kalorit.append(Summa)
            Summa = 0
            Rivi = Tiedosto.readline()
        elif Rivi != "\n":
            Summa += int(Rivi.strip())
            Rivi = Tiedosto.readline()

    Maksimi = max(Kalorit)
    print(Maksimi)
    Kalorit = sorted(Kalorit)

    KolmenSumma = sum(Kalorit[-3:])
    print(KolmenSumma)

paaohjelma()