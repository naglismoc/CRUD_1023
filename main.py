from data import load_holidays
from list_CRUD import *

holidays = load_holidays()

id_counter = 3
while True: #begalinis ciklas, kuris igalina funkcijos veikima vel ir vel
    print_info()
    option = input()
    match option: # vartotojo pasirinkimai ka gali daryti programoje
        case '1':
            print_holidays(holidays)
        case '2':
            id_counter = create_holidays(id_counter, holidays)
        case '3':
            edit_holidays(holidays)
        case '4':
            delete_holidays(holidays)
        case '5':
                break
