print("🌟Contact Card🌟")
print()


name = input("Input your name > ").strip()
print()
dob = input("Input your date of birth > ").strip()
print()
phone = input("Input your telephone number > ").strip()
print()
email = input("Input your email > ")
print()
address = input("Input your address > ")
print()

contact = {"name": name, "dob": dob, "phone": phone, "email": email, "address": address}

print(f"Hi {contact['name']}. Our dictionary says that you were born on {contact['dob']}, we can call you on {contact['phone']}, email {contact['email']}, or write to {contact['address']}.")  