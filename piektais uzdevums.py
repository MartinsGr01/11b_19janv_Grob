def ierakstit_vardu_faila(vards):
    try:
        with open('lietotajs.txt', 'w') as fails:
            fails.write(vards)
        print("Vārds veiksmīgi ierakstīts failā.")
    except IOError as e:
        print("Kļūda: Nevar ierakstīt failā. Pārliecinieties, vai jums ir rakstīšanas atļaujas.")
    except Exception as e:
        print("Kļūda:", e)
def galvena():
    try:
        vards = input("Ievadiet savu vārdu: ")
        ierakstit_vardu_faila(vards)
    except Exception as e:
        print("Kļūda:", e)
galvena()