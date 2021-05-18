# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#REZERVAČNÍ SYSTÉM


def uvod():
    print("="*40)
    text = "Vitej v programu".upper()
    print(text.center(40))
    print("="*40)
uvod()

def odradkovani():
    print("="*40)

def valid_vek():
    datum_narozeni = int(input("Zadejte rok narození: "))
    vek = ROK - datum_narozeni
    if vek < 18:
        print("Služby jsou pouze starším 18 let \n'UKONČUJI'...")
        exit()
    elif vek >= 18:
        print(input("Mužete pokračovat, stiskněte 'ENTER'..."))
    else:
        print("Chyba")
        exit()


def zadej_mesto():
    # mesto - vyhledání indexem, slovní zadání
    mesto = input("Zadejte název města, kam chcete jet: ")

    if mesto in MESTA:
        index_mesta = MESTA.index(mesto)
        destinace_mesto = MESTA[index_mesta]
        cena_mesto = CENY[index_mesta]

        if mesto in SLEVY:
            global sleva
            sleva = 0.75 * cena_mesto
            print("Do zadane lokality " + "'" + str(destinace_mesto) + "'"" mate slevu 25 %\nVýsledná cena je: " + str(sleva))
            odradkovani()
        else:
            sleva = cena_mesto

        #volání funkcí

        valid_jmeno()
        valid_prijmeni()
        valid_email()
        valid_heslo()

        odradkovani()

        #výpis
        print(f"Destinace: {destinace_mesto}")
        print(f"Cena: {sleva}")
        odradkovani()
        print("Registracní údaje".upper())
        odradkovani()

        print(f"Zadané jméno: {jmeno.upper()}")
        print(f"Zadané příjmení: {prijmeni.upper()}")
        print(f"E-mailová adresa: {email.upper()}")
        print(f"Heslo: {heslo.upper()}")

        exit()
    elif not mesto in MESTA:
        print("Zadané město není v nabídce.")
        odradkovani()
    else:
        print("Neplatny vstup")
        exit()



def valid_jmeno():
    global jmeno
    jmeno = input("Zadejte své jméno: ")
    if jmeno.isdigit() or jmeno.isnumeric() or len(jmeno) <=2:
        print("Jméno musí obsahovat pouze znaky a jeho délka musí být větší než 2")
        exit()
    elif not jmeno[0].isupper():
        print("Jméno musí začínat velkým písmem")
        exit()


def valid_prijmeni():
    global prijmeni
    prijmeni = input("Zadejte své příjmení: ")
    if prijmeni.isdigit() or prijmeni.isnumeric() or len(prijmeni) <=2:
        print("Příjmení musí obsahovat pouze znaky a jeho délka musí být větší než 2")
        exit()
    elif not prijmeni[0].isupper():
        print("Příjmení musí začínat velkým písmem")
        exit()

def valid_email():
    global email
    email = input("Zadejte svůj e-mail: ")
    if not "@" in email or not "." in email:
        print("E-mail není zadán správně")
        exit()
    elif email.count("@") > 1 or email.count(".") > 1:
        print("Chybný tvar e-mailu")
        exit()

def valid_heslo():
    global heslo
    heslo = input("Zadejte svoje heslo: ")
    if len(heslo) <=8 or heslo[0].isdigit() or heslo[0].isnumeric() or heslo[-1].isalpha():
        print("Chybný tvar hesla")
        exit()

#konstanty
MESTA = ["Praha", "Brno", "Olomouc", "Ostrava"]
CENY = [1000, 1200, 1300, 1100]
SLEVY = ["Praha", "Olomouc"]

ROK = 2021

print("Mužeme Vám nabídnou následujicí destinace: ")
print("""
1 - Praha      | 1000
2 - Brno       | 1200
3 - Olomouc    | 1300
4 - Ostrava    | 1100
""")
odradkovani()


#zadejte věk pro pokračování
valid_vek()
#formátování výstupu
odradkovani()

#zadejte název města, kam chcete jet
zadej_mesto()


cislo = int(input("Zadejte číslo destinace: "))

if cislo <= 0 or cislo > len(MESTA):
    print("Zadané číslo v nabídce není, \nUKONČUJI...")
    exit()
else:
    spravny_index = cislo - 1
    destinace = MESTA[spravny_index] #nebo kratším zápisem: destinace = MESTA[cislo-1]
    cena = CENY[spravny_index]

    if destinace in SLEVY:
        global sleva_index
        sleva_index = 0.75 * cena
        print(
            "Do zadane lokality " + "'" + str(destinace) + "'"" mate slevu 25 %\nVýsledná cena je: " + str(sleva_index))
        odradkovani()
    else:
        sleva_index = cena

#formatovani výstupu
odradkovani()
valid_jmeno()
valid_prijmeni()
valid_email()
valid_heslo()
odradkovani()

print(f"Destinace: {destinace.upper()}")
print("Cena: " + str(sleva_index))

odradkovani()
print("Registracní údaje".upper())
odradkovani()

print(f"Zadané jméno: {jmeno.upper()}")
print(f"Zadané příjmení: {prijmeni.upper()}")
print(f"E-mailová adresa: {email.upper()}")
print(f"Heslo: {heslo.upper()}")
