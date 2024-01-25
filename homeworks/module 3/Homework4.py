fimport datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date() # беремо сьогоднішню дату
    birthdays=[] # створюємо список для результатів
    for user in users: # перебираємо користувачів
        bdate=user["birthday"] # отримуємо дату народження людини у вигляді рядка
        bdate=str(tdate.year)+bdate[4:] # Замінюємо рік на поточний
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
        days_between=(bdate-tdate).days # рахуємо різницю між зараз і днем народження цьогоріч у днях
        if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні
            if week_day<6: #  якщо пн-пт
                birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
                # Додаємо запис у список.
            else:
                if (bdate+dt.timedelta(days=1)).weekday()==0:# якщо неділя
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
                elif (bdate+dt.timedelta(days=2)).weekday()==0: #якщо субота
                    birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
    return birthdays

print(get_upcoming_birthdays(users))