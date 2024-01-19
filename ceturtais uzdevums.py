def nolasit_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:\n", saturs)
    except FileNotFoundError:
        print("Fails tika atrasts.")
    except Exception as e:
        print("Kļūda:", e)
def galvena():
    try:
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")
        paplasinajums = input("Ievadiet faila paplašinājumu (piem., txt): ")
        pilns_faila_nosaukums = f"{faila_nosaukums}.{paplasinajums}"
        nolasit_failu(pilns_faila_nosaukums)
    except Exception as e:
        print("Kļūda:", e)
galvena()