accountAC1 = {"name" : "Kojo Sagoe", "age" : 14, "account_bal" : 0.32}
accountAC2 = {"name" : "Gloria Bobson", "age" : 10, "account_bal" : 50.63}

accounts =[accountAC1, accountAC2]

count = 1
for account in accounts:
    print(f"\nAccountAC{count}:")
    for account_details in account.items():
        print(f"{account_details[0]} : {account_details[1]}")
    count += 1