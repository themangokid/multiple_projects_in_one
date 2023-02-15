def get_month_name(month_number):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[month_number - 1]

def get_day_suffix(day):
    if 11 <= day <= 13:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')

def format_date(date):
    month_number, day, year = date.split('/')
    month_name = get_month_name(int(month_number))
    day_suffix = get_day_suffix(int(day))
    return f"{month_name} {day}{day_suffix}, {year}"

# Add numbers for each month
for i, month in enumerate(get_month_name(n) for n in range(1, 13)):
    print(f"{i+1}. {month}")

dates = ['01/01/2022', '05/11/2022', '12/31/2022']

for date in dates:
    print(format_date(date))
