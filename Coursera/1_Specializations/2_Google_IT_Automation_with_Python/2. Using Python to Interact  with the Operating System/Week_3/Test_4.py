import re


def transform_comments(line_of_code):
    result = re.sub(r'(#+)', r'//', line_of_code)
    return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

text = "We arrive on 03/25/2018. So you are welcome after 04/01/2018."
print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text))


def convert_phone_number(phone):
    result = re.sub(r' (\d+)-(\d+)(-\d+)', r' (\1) \2\3', phone)
    return result


print(convert_phone_number(
    "My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number(
    "Please call 888-555-1234"))  # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))  # 123-123-12345
print(convert_phone_number(
    "Phone number of Buckingham Palace is +44 303 123 7300"))
# Phone number of Buckingham Palace is +44 303 123 7300
