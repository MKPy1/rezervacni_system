# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#REZERVAČNÍ SYSTÉM
#TRÉNINKOVÉ PROGRAMY
#upper,lower,split,strip,replace,casefold,title,swapcase,expandtabs,center,startswith,endswith

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

"""
# staticke opakovani
def odradkovani():
    print("=" * 40)
    novy_string = str("Vítej v proramu")
    print(novy_string + "\n" + "=" * 40)
odradkovani()


def jmeno_valid():
    if (len(jmeno) <= 1 or len(jmeno) > 10) and not jmeno.isdigit():
        print("Jmeno - chyba")
        exit()


def prijmeni_valid():
    if (len(prijmeni) <= 1 or len(prijmeni) > 10) and not prijmeni.isdigit():
        print("Prijemni - chyba")
        exit()


def datum_valid():
    global vek
    vek = AKTUALNI_ROK - datum_narozeni
    if vek < 18:
        print("Mladsi nez 18 let mají zákaz, ukoncuji...")
        exit()


def email_valid():
    if len(email) < 0 and not email.startswith(CISLA_ZACATEK):
        print("Kratky e-mail")
        exit()
    elif not email.count(".") == 1 or not email.count("@") == 1:
        print("Chybny format e-mailu")
        exit()

def heslo_valid():
    if len(heslo) <=8 or heslo.startswith(CISLA_ZACATEK):
        print("Heslo je příliš krátké nebo začíná nepovolenými znaky")
        exit()
    elif heslo.count("@") < 1 or heslo in VELKE < 1: #heslo.isupper()
        print("Heslo musí obsahovat alespoň 1 velké písmeno a také speciální znak @")
        exit()



# konstanty, tuple pro nemennost
MESTA = ("Praha", "Vídeň", "Brno", "Svitavy", "Zlín", "Ostrava")
CENA = (1000, 1100, 2000, 1500, 2300, 3400)
INTERVAL = ("1", "2", "3", "4", "5", "6")
ZAKAZ = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y", "z")
AKTUALNI_ROK = 2021
SLEVA = (0.75, 0.75, 0.25, 0.5, 0.25, 0.6)

POVOLENE_ZNAKY = (".", "@", "cz")
CISLA_ZACATEK = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
VELKE = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z")

mesto_destinace = input("Zadej mesto: ")
if mesto_destinace in MESTA:
    index = MESTA.index(mesto_destinace)
    destinace = MESTA[index]
    cena = CENA[index]
    print("Zadane mesto je v nabidce, pokracuji...")
    print(f"Zadane mesto je: {destinace}")
    print(f"Cena je: {cena}")
    print("=" * 40)
else:
    print("Nenalezeno, zkuste zadat cislo destinace...")
    print("=" * 40)
    cislo_destinace = input("Zadej cislo destinace: ")

    if cislo_destinace in ZAKAZ:
        print("Napovolený znak na vstupu")
        exit()

    elif cislo_destinace in INTERVAL:
        spravny_index = int(cislo_destinace) - 1
        destinace = MESTA[spravny_index]
        cena = CENA[spravny_index]
        sleva = SLEVA[spravny_index]

        jmeno = input("Zadej jméno: ")
        if jmeno.isdigit():
            print("Byl zadán chybný vstup")
            exit()
        else:
            jmeno_valid()

            prijmeni = input("Zadej příjmení: ")
            prijmeni_valid()

            datum_narozeni = int(input("Zadej datum narození: "))
            datum_valid()

            email = input("Zadej e-mail: ")
            email_valid()

            heslo = input("Zadej heslo: ")
            heslo_valid()

            print("Do zadane destinace " + str(destinace) + " " + "je nabizena sleva: " + str(sleva) + ", " + "pokracuji...")
            vysledna_cena = cena * sleva
            print("Vysledna cena je: " + str(vysledna_cena))

            print("=" * 40)
            print(f"Jméno a příjmení: {jmeno} {prijmeni}")
            print("Datum narození je: " + str(datum_narozeni))
            print("E-mailová adresa je: ", email)
            print("Hesloa je: ", heslo)
    else:
        print("Neplatný vstup")
        exit()
"""
"""
#vypocet Pythagorovy vety
def pythagoras():
    a=float(input("Zadej cislo a: "))
    b=float(input("Zadej cislo b: ")) 
    global c
    c = float(math.sqrt(a*a + b*b))
    vysledek = "Vysledek je : {}" #print(c)
    print(vysledek.format(c))
pythagoras()

#** je umocneni, cislo na kolikatou (2)
def obsah_kruhu():
    r=float(input("Zadej hodnotu r: "))
    global obsah
    obsah = float(math.pi * r**2)
    vysledek2 = "Vysledek 2 je: {}"#print(obsah)
    print(vysledek2.format(obsah))
obsah_kruhu()

def porovnej_pythagora_obsah():
    if c > obsah:
        print("Pythagoras je vetsi nez obsah")
    elif obsah > c:
        print("Obsah je vetsi nez pythagoras")
    else:
        print("Rovnost")
porovnej_pythagora_obsah()


#funkce pro porovnani delky retezce
def prvni_retezec():
    global prvni
    prvni = str("AHOJKY")
    print(len(prvni))
prvni_retezec()

def druhy_retezec():
    global druhy
    druhy = str("CAUKY")
    print(len(druhy))
druhy_retezec()

def porovnej():
    if prvni > druhy:
        print("Prvni je vetsi ")
    elif druhy > prvni:
        print("Druhy je vetsi ")
    else:
        print("ROVNOST")
porovnej()

#funkce pro porovnani delky retezcu
def vysledek():
    global znak,znak2
znak = str("JJ")
znak2 = str("mee")

if (len(znak) > len(znak2)):
    print("Delsi je " + znak)
elif (len(znak2) > len(znak)):
    print("Delsi je " + znak2)
else:
    print("Znaky " + znak + "a " + znak2 + " jsou stejne dlouhe")
vysledek()

#funkce pro porovnani obsahu a obvodu
def obsah():
    a=int(5)
    b=int(6)
    global vysledek
    vysledek=a*b
    vypis = "Vysledek je: {}"
    print(vypis.format(vysledek))  
obsah()

def obvod():
    a=int(5)
    b=float(5.2)
    global vysledek2
    vysledek2 = float(b/a)
    vypis = "Vysledek je: {}"
    print(vypis.format(vysledek2))
obvod()

if vysledek > vysledek2:
    print("Vetsi je: obsah")
elif vysledek2 > vysledek:
    print("Vetsi je: obvod")
else:
    print("ROVNOST")
"""

