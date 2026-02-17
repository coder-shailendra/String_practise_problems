def defanginganIPadress(address):
    return address.replace(".", "[.]")
print(defanginganIPadress("1.1.1.1"))
print(defanginganIPadress("255.100.50.0"))
