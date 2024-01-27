import random

def get_numbers_ticket(min, max, quantity):
    if (max < min ):
        return False
    for num in [min, max, quantity]:
        if not (1 <= num <= 1000):
            return False
        uniq_numbs = random.sample(range(min, max + 1), quantity)
        return sorted(uniq_numbs)
lottery_numbers = get_numbers_ticket(1,49,6)
print("Ваші лотерейні числа:", lottery_numbers)
