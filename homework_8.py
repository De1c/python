from datetime import datetime, date, timedelta
from time import strftime

def get_birthdays_per_week(users):
    
    final_res = {}  #Dict for birthdays
    my_list = []
    today = date.today()
    delta = timedelta(days=7)
    for user in users:
        if delta.days >= (user['birthday'] - today).days and (user['birthday'] - today).days >= 0:
            try:
                final_res[user['birthday'].strftime('%A')] += user['name'] + ' '
            except KeyError:
                final_res[user['birthday'].strftime('%A')] = user['name'] + ' '
    #If birthday in weekend's, move to monday
    if 'Saturday' in final_res:
        if 'Monday' in final_res:
            final_res['Monday'] += final_res.pop('Saturday')
        else:
            final_res['Monday'] = final_res.pop('Saturday')
    if 'Sunday' in final_res:
        if 'Monday' in final_res:
            final_res['Monday'] += final_res.pop('Sunday')
        else:
            final_res['Monday'] = final_res.pop('Sunday')
    #Final print
    for i in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
        try:
            my_list.append(f'{i}: {", ".join((final_res[i].strip()).split())}')
        except KeyError:
            continue
    print(my_list)

if __name__ == '__main__':
    my_users = [
        {
            'name': 'Mark', 'birthday': date(year=datetime.now().year, month=9, day=28)
        },
        {
            'name': 'Gleb', 'birthday': date(year=datetime.now().year, month=8, day=23)
        },
        {
            'name': 'Arthem', 'birthday': date(year=datetime.now().year, month=9, day=20)
        },
        {
            'name': 'Sanya', 'birthday': date(year=datetime.now().year, month=9, day=28)
        },
        {
            'name': 'Vanya', 'birthday': date(year=datetime.now().year, month=9, day=24)
        },
        {
            'name': 'Raf', 'birthday': date(year=datetime.now().year, month=10, day=28)
        },
        {
            'name': 'Danya', 'birthday': date(year=datetime.now().year, month=9, day=25)
        },
        {
            'name': 'Liza', 'birthday': date(year=datetime.now().year, month=9, day=29)
        },
        {
            'name': 'Lena', 'birthday': date(year=datetime.now().year, month=9, day=27)
        },
    ]
    print(get_birthdays_per_week(my_users))