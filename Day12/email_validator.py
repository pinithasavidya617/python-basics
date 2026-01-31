def email_validator(email):
    if "@" not in email:
        return False
    if email.startswith('@') or email.endswith('@') or email != email.lower():
        return False
    else:
        return True

in_email = input("Enter email: ")
if email_validator(in_email):
    print("Valid")
else:
    print("Invalid")