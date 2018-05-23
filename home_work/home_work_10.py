
def gravestone_labeler(text):
    name = text.split('*')[0]
    birth_date = text.split('*')[1].split('-')[0]    #
    death_date = text.split('*')[2].split('-')[0]    # Не читабельно(
    lifetime = int(death_date) - int(birth_date)     # Зато работает)
    return name + ', ' + str(lifetime)
