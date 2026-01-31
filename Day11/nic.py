
nic = input("Enter NIC num: ").lower()

if len(nic) == 11:
    valid_nic = nic[:10]
    if valid_nic.isdigit() and nic.endswith("v"):
            print("NIC valid")
    else:
            print("Invalid!")
else:
    print("Invalid!")

