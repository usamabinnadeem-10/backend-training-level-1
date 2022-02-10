birthdays = [
    {
        'name': 'Harry Potter',
        'birthday': {
            'day': '10',
            'month': '03',
            'year': '1993'
        }
    },
    {
        'name': 'Ronald Weasley',
        'birthday': {
            'day': '15',
            'month': '12',
            'year': '1992'
        }
    },
    {
        'name': 'Hermoine Granger',
        'birthday': {
            'day': '02',
            'month': '09',
            'year': '1994'
        }
    }
]


def main():
    print('>>> Welcome to the birthday dictionary. We know the birthdays of:')
    for person in birthdays:
        print(person['name'])
    input_name = input('>>> Who\'s birthday do you want to look up?')
    filtered = list(filter(lambda person: person['name'] == input_name, birthdays))
    if (len(filtered) > 0):
        filtered = filtered[0]
        print(f""">>> {filtered['name']}'s birthday is {filtered['birthday']['day']}/{filtered['birthday']['month']}/{filtered['birthday']['year']}.""")
    else:
        print('Oops, could not find the birthday')
    pass

if __name__ == '__main__':
    main()