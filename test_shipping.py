import shipping
import shipping_mongo

def test_validate_invalid_numbers():
    assert shipping.validate('5',1,2) is False

def test_validate_valid_numbers():
    assert shipping.validate('3',1,5) is True

def test_validate_valid_name():
    assert shipping.validate('Shayda',5,20) is True

def test_validate_invalid_name():
    assert shipping.validate('ShaydaShaydaShaydaShayda', 5, 20) is False

def test_validate_valid_booking():
    booking_data_before = {
        'first_name': {'prompt': 'Enter first name. ', 'value': 'Shayda', 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'last_name': {'prompt': 'Enter last name. ', 'value': 'Banihashemi', 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'description': {'prompt': 'Enter package description. ', 'value': 'TESTTESTTEST', 'min_val': 5, 'max_val': 40,
                        'is_valid': False},
        'dangerous': {'prompt': 'Are the package contents dangerous. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                      'is_valid': False},
        'urgent': {'prompt': 'Is this shipment urgent. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                   'is_valid': False},
        'international': {'prompt': 'Is this shipment international. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                          'is_valid': False},
        'weight': {'prompt': 'Enter the weight. ', 'value':  '5', 'min_val': 0, 'max_val': 10, 'is_valid': False},
        'length': {'prompt': 'Enter the length. ', 'value': '5', 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'width': {'prompt': 'Enter the width. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'height': {'prompt': 'Enter the height. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': False},
    }
    booking_data_after = {
        'first_name': {'prompt': 'Enter first name. ', 'value': 'Shayda', 'min_val': 5, 'max_val': 20, 'is_valid': True},
        'last_name': {'prompt': 'Enter last name. ', 'value': 'Banihashemi', 'min_val': 5, 'max_val': 20, 'is_valid': True},
        'description': {'prompt': 'Enter package description. ', 'value': 'TESTTESTTEST', 'min_val': 5, 'max_val': 40,
                        'is_valid': True},
        'dangerous': {'prompt': 'Are the package contents dangerous. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                      'is_valid': True},
        'urgent': {'prompt': 'Is this shipment urgent. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                   'is_valid': True},
        'international': {'prompt': 'Is this shipment international. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                          'is_valid': True},
        'weight': {'prompt': 'Enter the weight. ', 'value':  '5', 'min_val': 0, 'max_val': 10, 'is_valid': True},
        'length': {'prompt': 'Enter the length. ', 'value': '5', 'min_val': 0, 'max_val': 5, 'is_valid': True},
        'width': {'prompt': 'Enter the width. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': True},
        'height': {'prompt': 'Enter the height. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': True},
    }
    assert shipping_mongo.validate_input(booking_data_before) == (booking_data_after, True)

def test_validate_invalid_booking():
    booking_data_before = {
        'first_name': {'prompt': 'Enter first name. ', 'value': 'Sha', 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'last_name': {'prompt': 'Enter last name. ', 'value': 'Banihashemi', 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'description': {'prompt': 'Enter package description. ', 'value': 'TESTTESTTEST', 'min_val': 5, 'max_val': 40,
                        'is_valid': False},
        'dangerous': {'prompt': 'Are the package contents dangerous. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                      'is_valid': False},
        'urgent': {'prompt': 'Is this shipment urgent. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                   'is_valid': False},
        'international': {'prompt': 'Is this shipment international. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                          'is_valid': False},
        'weight': {'prompt': 'Enter the weight. ', 'value':  '5', 'min_val': 0, 'max_val': 10, 'is_valid': False},
        'length': {'prompt': 'Enter the length. ', 'value': '5', 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'width': {'prompt': 'Enter the width. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': False},
        'height': {'prompt': 'Enter the height. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': False},
    }
    booking_data_after = {
        'first_name': {'prompt': 'Enter first name. ', 'value': 'Sha', 'min_val': 5, 'max_val': 20, 'is_valid': False},
        'last_name': {'prompt': 'Enter last name. ', 'value': 'Banihashemi', 'min_val': 5, 'max_val': 20, 'is_valid': True},
        'description': {'prompt': 'Enter package description. ', 'value': 'TESTTESTTEST', 'min_val': 5, 'max_val': 40,
                        'is_valid': True},
        'dangerous': {'prompt': 'Are the package contents dangerous. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                      'is_valid': True},
        'urgent': {'prompt': 'Is this shipment urgent. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                   'is_valid': True},
        'international': {'prompt': 'Is this shipment international. [Y/N] ', 'value': 'Y', 'min_val': 1, 'max_val': 1,
                          'is_valid': True},
        'weight': {'prompt': 'Enter the weight. ', 'value':  '5', 'min_val': 0, 'max_val': 10, 'is_valid': True},
        'length': {'prompt': 'Enter the length. ', 'value': '5', 'min_val': 0, 'max_val': 5, 'is_valid': True},
        'width': {'prompt': 'Enter the width. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': True},
        'height': {'prompt': 'Enter the height. ', 'value': '3', 'min_val': 0, 'max_val': 5, 'is_valid': True},
    }
    assert shipping_mongo.validate_input(booking_data_before) == (booking_data_after, False)


