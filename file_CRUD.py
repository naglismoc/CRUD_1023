
import csv

headers = ['id','country','city','price','accomodation']
def load_holidays():
    with open("holidays.csv",mode='r',encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_holidays(holidays):
    with open('holidays.csv',mode='w',newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(holidays)

def create_holidays(id_counter, holidays):
    print("pridedu nauja")
    print("Iveskite sali")
    country = input()
    print("Iveskite miesta")
    city = input()
    print("Iveskite apgyvendinimo tipo")
    accom = input()
    print("Iveskite kaina")
    price = float(input())
    id_counter += 1
    hol = {'id': id_counter, "country": country, "city": city, "price": price, "accomodation": accom}
    holidays.append(hol)
    save_holidays(holidays)
    return id_counter


def edit_holidays(holidays):
    print_holidays(holidays)
    print("iveskite id iraso kuri nori redaguoti")
    edit_id = input()
    for hol in holidays:
        if edit_id == str(hol['id']):
            print("Iveskite sali")
            hol['country'] = input()
            print("Iveskite miesta")
            hol['city'] = input()
            print("Iveskite apgyvendinimo tipo")
            hol['accomodation'] = input()
            print("Iveskite kaina")
            hol['price'] = float(input())
            break
    save_holidays(holidays)

def delete_holidays(holidays):
    print_holidays(holidays)
    print("iveskite id iraso kuri nori trinti")
    del_id = input()
    for hol in holidays:
        if del_id == str(hol['id']):
            pos = holidays.index(hol)
            del holidays[pos]
            break
    save_holidays(holidays)


def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
def print_holidays(holidays):
    for hol in holidays:
        print(
            f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")