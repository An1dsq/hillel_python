
def date_to_normal(date):
    list_date = date.split('.')
    international_date = list_date[1] + '.' + list_date[0] + '.' + list_date[2]  # Выглядит раково
    return international_date
