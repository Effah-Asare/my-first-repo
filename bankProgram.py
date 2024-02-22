account001 = {"name" : "Kojo Sagoe", "age" : 14, "account_bal" : 0.32}
account002 = {"name" : "Gloria Bobson", "age" : 10, "account_bal" : 50.63}

accounts =[account001, account002]

count = 1
for account in accounts:
    print(f"\nAccount00{count}:")
    for account_details in account.items():
        print(f"{account_details[0]} : {account_details[1]}")
    print()
    count += 1