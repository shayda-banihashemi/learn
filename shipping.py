import datetime

today = datetime.date.today()
print (today)
todays_number = today.weekday()

def get_input(booking_data):
    for field_name, field_data in booking_data.items():
        if not field_data['is_valid']:
            if not field_data['value'] is None:
                print("The value you entered was invalid, please re-enter. ")
            field_data['value'] = input(field_data['prompt'])
    return booking_data

def validate(value: str, min_val, max_val):
    if value.isnumeric():
        value = float(value)
        if not (min_val <= value <= max_val):
            return False
        return True

    if not (min_val <= len(value) <= max_val):
        return False
    return True

def validate_input(booking_data):
    all_fields_valid = True
    for field_name, field_data in booking_data.items():
        field_data['is_valid'] = validate(field_data['value'], field_data['min_val'], field_data['max_val'] )
        if not field_data['is_valid']:
            all_fields_valid = False

    return booking_data, all_fields_valid

def main():
    booking_data = {
        'first_name': {'prompt': 'Enter first name. ', 'value': None, 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'last_name': {'prompt': 'Enter last name. ', 'value': None, 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'description': {'prompt': 'Enter package description. ', 'value': None, 'min_val': 5, 'max_val': 40,
                        'is_valid': False},
        'dangerous': {'prompt': 'Are the package contents dangerous. [Y/N] ', 'value': None, 'min_val': 1, 'max_val': 1,
                      'is_valid': False},
        'urgent': {'prompt': 'Is this shipment urgent. [Y/N] ', 'value': None, 'min_val': 1, 'max_val': 1,
                   'is_valid': False},
        'international': {'prompt': 'Is this shipment international. [Y/N] ', 'value': None, 'min_val': 1, 'max_val': 1,
'is_valid': False},
        'weight': {'prompt': 'Enter the weight. ', 'value': None, 'min_val': 0, 'max_val': 10, 'is_valid': False},
        'length': {'prompt': 'Enter the length. ', 'value': None, 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'width': {'prompt': 'Enter the width. ', 'value': None, 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'height': {'prompt': 'Enter the height. ', 'value': None, 'min_val': 0, 'max_val': 5, 'is_valid': False},
    }

    while True:
        booking_data = get_input(booking_data)
        validated_booking_data, all_fields_valid = validate_input(booking_data)
        print(validated_booking_data)

        if all_fields_valid:
            break

if __name__ == "__main__":
    main()









