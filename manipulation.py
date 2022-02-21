import json
from collections import Counter

def ask_choice():
    return input('\n>>> Press 1 if you want to look up a birthday\n>>> Press 2 if you want to add a birthday\n>>> Enter any other key to quit\n')

def show_birthdays(birthdays):
    print('>>> Welcome to the birthday dictionary. We know the birthdays of:\n')
    for person in birthdays:
        print(person['name'])

with open('./birthdays.json', 'r') as f:
  data = json.load(f)

birthdays = data['birthdays']

def filter_even():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print('\nOriginal list ==> ', a)
    print('Even list ==> ', list(filter(lambda val: val % 2 == 0, a)))

def group_birthdays():
    month_names = data['month_names']
    grouped = list(Counter([month_names[person['birthday']['month']] for person in birthdays]).items())
    print('\n>>> Number of people having birthdays in the same months')
    print(grouped,'\n')

def main():
    show_birthdays(birthdays)
    choice = None
    choice = ask_choice()
    quit = False
    while(not quit):
        if choice == '1':
            input_name = input('>>> Enter the name of person\n')
            filtered = list(filter(lambda person: person['name'] == input_name, birthdays))
            if (len(filtered) > 0):
                filtered = filtered[0]
                print(f""">>> {filtered['name']}'s birthday is {filtered['birthday']['day']}/{filtered['birthday']['month']}/{filtered['birthday']['year']}.""")
            else:
                print('Oops, could not find the birthday')
            choice = ask_choice()
        elif choice == '2':
            person_name = input('>>> Enter the name: ')
            day = input('>>> Enter the day : ')
            month = input('>>> Enter the month : ')
            year = input('>>> Enter the year : ')
            data = {
                "name": person_name,
                "birthday": {
                    "day": day,
                    "month": month,
                    "year": year
                }
            }
            birthdays.append(data)
            out_file = open("./birthdays.json", "w")
            json.dump({'birthdays': birthdays}, out_file, indent=4)
            show_birthdays(birthdays)
            choice = ask_choice()
        else:
            quit = True

if __name__ == '__main__':
    filter_even()
    group_birthdays()
    main()