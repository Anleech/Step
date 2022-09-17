import re


def validate_phone(name):
    reg = r"^\+?7[ (]*\d+[ )]*[\d -]{8,10}"
    return re.search(reg, name).group()

print(validate_phone('+7 499 456-45-78'))
print(validate_phone('+74994564578'))
print(validate_phone('7 (499) 456-45-78'))
print(validate_phone('7 (499) 456-45-78'))
