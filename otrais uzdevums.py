import csv
def nolasit_otro_kolonnu(csv_faila_nosaukums):
    try:
        with open(csv_faila_nosaukums, 'r') as csv_fails:
            lasitajs = csv.reader(csv_fails)
            for rindina in lasitajs:
                if len(rindina) > 1:
                    print(rindina[1])
                else:
                    print("Rindina nav pietiekami garša, lai izdrukātu otro kolonnu.")
    except FileNotFoundError:
        print("Fails tika atrasts.")
    except Exception as e:
        print("Kļūda:", e)
nolasit_otro_kolonnu('dati.csv')