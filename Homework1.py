from datetime import datetime
# def get_days_from_today(date):
    
try:
    converted_date = input("Введість дату в форматі yyyy-mm-dd: ")
    converted_date = datetime.strptime(converted_date, "%Y-%m-%d")
    current_date = datetime.today()            
    result = converted_date.toordinal() - current_date.toordinal()
    print({result})
    

except Exception as e:
        print (f"Error: {e}")
finally:
        pass




import random