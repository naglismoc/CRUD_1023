import pymysql

DB_CONFIG = {
    'host':"localhost",
    'port':3312,
    'user':'root',
    'password':'root',
    'database':'holidays'
}

headers = ['id','country','city','accomodation','price']
def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_holidays():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays")
    rows = cur.fetchall()
    conn.close()
    cur.close()
    holidays = []
    for row in rows:
        holiday = {}
        for i in range(len(headers)):
            holiday[headers[i]] = row[i]
        holidays.append(holiday)
    return holidays

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
    # id_counter += 1
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO `holidays` (`country`,`city`,`accomodation`,`price`) VALUES (%s,%s,%s,%s);",
        (country, city,accom, price)
    )
    conn.commit()
    cur.close()
    conn.close()
    return id_counter

def edit_holidays(holidays):
    print_holidays(holidays)
    print("iveskite id iraso kuri nori redaguoti")
    edit_id = input()
    print("Iveskite sali")
    country = input()
    print("Iveskite miesta")
    city = input()
    print("Iveskite apgyvendinimo tipo")
    accom = input()
    print("Iveskite kaina")
    price = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE `holidays` SET `country` = %s, `city` =%s,`accomodation` = %s, `price` = %s WHERE `id` = %s;",
        (country,city,accom,price,edit_id)
    )
    conn.commit()
    cur.close()
    conn.close()
def delete_holidays(holidays):
    print_holidays(holidays)
    print("iveskite id iraso kuri nori trinti")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM `holidays` WHERE `id` = %s;",
        (del_id,) #BŪTINAI REIKIA KABLELIO, KAD TRAKTUOTŲ KAIP TUPPLE, O NE APSKLIAUSTĄ REIKŠMĘ!
    )
    conn.commit()
    cur.close()
    conn.close()

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
def print_holidays(holidays):
    holidays = load_holidays()
    for hol in holidays:
        print(
            f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")