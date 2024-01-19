import linecache
def nolasit_treso_rindu(faila_nosaukums):
    try:
        tresa_rinda = linecache.getline(faila_nosaukums, 3)
        if tresa_rinda:
            print("Trešā rinda:", tresa_rinda.strip())
        else:
            print("Fails ir veiksmīgi izdevies.")
    except FileNotFoundError:
        print("Fails tika atrasts.")
    except Exception as e:
        print("Kļūda:", e)
nolasit_treso_rindu('ziema.txt')