from omamodul import *
ikood=""
arvud=["100","1001","211","222"] 
ikoodid=[]
while True:
    ikood=input("Sisesta isikukood: ")
    if ikood=="-": break
    if pikkus(ikood)==False:
        print("Liiga pikk v�i l�hikese isikukood")
        arvud.append(ikood)
    else:
        print("11 s�mbilid")
        s=esimine(ikood)
        if s=="viga":
            print("Esimene t�ht ei ole �ige")
            arvud.append(ikood)
        else:
            print(s)
            if sunnipaev(ikood)=="viga":
                print("2-7 t�hed on valesti sisestatud")
            else:
                lause(ikood) 
                if kontrollnr(ikood)==int(ikood[-1]):
                    print("OK")
                    ikoodid.append(ikood)
                else:
                    print("!!!")
print()
naised_mehed(ikoodid)
print(ikoodid)
arvud_sorted(arvud)
print(arvud)