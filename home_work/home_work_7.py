
def date_to_normal(date):
    list_date = date.split('.')
    list_date[0], list_date[1] = list_date[1], list_date[0]
    international_date = '.'.join(list_date)
    return international_date
