import re
def extract_number(input):
    phone_regex= re.compile(r'/b/d{3} /d{3}-/d{4}/b')
    match = phone_regex.search(input)
    if match :
        return match.group()
    else :
        return None

def extract_all_numbers(input):
    phone_regex= re.compile(r'/b/d{3} /d{3}-/d{4}/b')
    return phone_regex.findall(input)

def is_valid_number(input):
    phone_regex= re.compile(r'^/d{3} /d{3}-/d{4}$')
    match = phone_regex.search(input)
    if match :
        return True
    else :
        return False

print(is_valid_number("432 567-8976"))