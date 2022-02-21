import collections


class CustomException(BaseException):
    """Custom exception class for raising custom exceptions"""

    def __init__(self, message='Username is not unique'):
        super().__init__(message)

    @classmethod
    def invalid_age(cls):
        return cls('Age is not a positive integer')

    @classmethod
    def under_age(cls):
        return cls('Age is less than 16')

    @classmethod
    def invalid_email(cls):
        return cls('Email is invalid')


data = [
    {
        'username': 'usama.nadeem',
        'age': 20,
        'email': 'usama.nadeem@carteblanche.tech',
    },
    {
        'username': 'usama.nadeem',
        'age': -2,
        'email': 'usama.nadeem2@carteblanche.tech',
    },
    {
        'username': 'usama.nadeem3',
        'age': 10,
        'email': 'usama.nadeem3@carteblanche.tech',
    },
    {
        'username': 'usama.nadeem',
        'age': 18,
        'email': 'usama.nadeem',
    },
    {
        'username': 'usama',
        'age': 25,
        'email': 'usama@carteblanche.tech',
    },
]

def is_age_invalid(age):
    if age < 16:
        print(CustomException.under_age())
        return False
    return True
    

def is_age_negative(age):
    if age < 0:
        print(CustomException.invalid_age())
        return False
    return True

def is_email_invalid(email):
    if email.count('@') != 1 or len(email.split('@')) != 2:
        print(CustomException.invalid_email())
        return False
    return True


def test_data(user_data):
    return (
        is_age_negative(user_data['age']) and
        is_age_invalid(user_data['age']) and
        is_email_invalid(user_data['email'])
    )

def print_final_result(collection):
    print('\n---- Final Collection ----\n')
    for c in collection:
        print(f"username: {c} | age: {collection[c]['age']} | email: {collection[c]['email']}")

def print_initial_data(data):
    print('\n---- Original Data ----\n')
    for d in data:
        print(f"username: {d['username']} | age: {d['age']} | email: {d['email']}")
    print('\n')

def main():
    print_initial_data(data)
    collection = collections.defaultdict(str)
    for d in data:
        if test_data(d):
            if d['username'] in collection:
                print(CustomException())
            else:
                collection[d['username']] = d
    print_final_result(collection)


if __name__ == '__main__':
    main()

    

    