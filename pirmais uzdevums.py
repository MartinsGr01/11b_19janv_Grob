def lasit_un_drukats(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:\n", saturs)
    except FileNotFoundError:
        print("Pārbaudes darbs.")
    except Exception as e:
        print("Kļūda:", e)
lasit_un_drukats('pārbaudes darbs.txt')