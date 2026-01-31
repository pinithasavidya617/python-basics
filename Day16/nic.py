from datetime import datetime

class Student:
    def __init__(self, nic, first_name):
        self.nic = nic
        self.first_name = first_name

    def get_birthday(self):
        nic_for_birthday = self.nic.strip().upper()


        if len(nic_for_birthday) == 12:
            birth_year = int(nic_for_birthday[0:4])
            day_of_year = int(nic_for_birthday[4:7])
            if day_of_year >= 59:
                day_of_year -= 1

        elif len(nic_for_birthday) == 10 and nic_for_birthday[-1] in ("V", "X"):
            birth_year = 1900 + int(nic_for_birthday[0:2])
            day_of_year = int(nic_for_birthday[2:5])
            day_of_year -= 1
        else:
            return "Invalid NIC"

        try:
            if day_of_year > 500:
                day_of_year -= 500

            if not (1 <= day_of_year <= 366):
                return "Invalid NIC"

            date_str = f"{birth_year}{day_of_year:03d}"
            birthday = datetime.strptime(date_str, "%Y%j")
            return birthday.strftime(f"{self.first_name}'s birthday : %Y-%m-%d")
        except ValueError:
            return "Invalid NIC!"

# --- Test NICs ---
test_nics = [
    ("731252254V", "SS"),  #may4
    ("200021708323", "Bob"),  #aug4
    ("200132300540", "Charlie"), #aug5
    ("721252254V", "Poloe"),  #may3
    ("200430001669", "Pini"),  # jan 7
    ("200515903206", "VV")  # june 7

]

for nic, name in test_nics:
    student = Student(nic, name)
    print(student.get_birthday())
