from datetime import datetime
def get_days_from_today(date):
       while True:    
           try:
                 converted_date = datetime.strptime(date, "%Y-%m-%d")
                 current_date = datetime.today()            
                 difference  = converted_date.toordinal() - current_date.toordinal()
                 return difference
           except ValueError:
                 print("Невірний формат вводу")
                 date = input("Введість дату в форматі yyyy-mm-dd: ")
                 continue
           else:
                 break

date = input("Введість дату в форматі yyyy-mm-dd: ")           
result = get_days_from_today(date)
print({result})
    