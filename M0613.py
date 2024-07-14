import datetime

with open('today.txt', 'w') as file:
    file.write(str(datetime.date.today()))

with open('today.txt', 'r') as file:
    today_string = file.read()

parsed_date = datetime.strptime(today_string, '%Y-%m-%d')