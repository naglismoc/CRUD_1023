holidays = [ # startiniai duomenys
            {
                'id': 1,
                "country":"Lithuania",
                "city":"Palanga",
                "price":20.0,
                "accomodation":"hotel"
            },
            {
                'id': 2,
                "country":"Turkija",
                "city":"Alanya",
                "price":60.0,
                "accomodation":"hostel"
            },
            {
                'id': 3,
                "country":"Cyprus",
                "city":"Larnaka",
                "price":70.0,
                "accomodation":"apartaments"
            }
        ]

id_counter = 3
while True: #begalinis ciklas, kuris igalina funkcijos veikima vel ir vel
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    option = input()
    match option: # vartotojo pasirinkimai ka gali daryti programoje
        case '1':
            print("va, atostogos")
            for hol in holidays:
                print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")
        case '2':
            print("pridedu nauja")
            print("Iveskite sali")
            country = input()
            print("Iveskite miesta")
            city = input()
            print("Iveskite apgyvendinimo tipo")
            accom = input()
            print("Iveskite kaina")
            price = float(input())
            id_counter +=1
            hol = {'id': id_counter, "country":country, "city":city, "price":price, "accomodation":accom}
            holidays.append(hol)
        case '3':
            for hol in holidays:
                print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")
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
        case '4':
            for hol in holidays:
                print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")
            print("iveskite id iraso kuri nori trinti")
            del_id = input()
            for hol in holidays:
                if del_id == str(hol['id']):
                    print(hol)
                    pos = holidays.index(hol)
                    del holidays[pos]
                    break
        case '5':
                break
