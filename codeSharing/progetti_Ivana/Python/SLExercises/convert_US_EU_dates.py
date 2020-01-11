import calendar
import re

month_names = []
for i in range(1,13):
    month_names.append(calendar.month_name[i])
print(month_names)
def get_EU_date(US_date):
    match_month = re.search(r"([A-Za-z]+)",US_date)
    if not match_month:
        month=US_date[0:2]
        match_day = re.search(r"(/)(\d+)(/)", US_date)
        match_year = re.search(r"(/)(\d+)$", US_date)
    else:
        month=str(month_names.index(match_month.group())+1)
        match_day = re.search(r"( |.)(\d+)(,)", US_date)
        match_year = re.search(r"(,)(\d+)$", US_date)
    day = match_day.group(2)
    year = match_year.group(2)
    EU_date=day+"/"+month+"/"+year

    return EU_date

print(get_EU_date(input()))