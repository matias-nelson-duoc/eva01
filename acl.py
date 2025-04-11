acl = int(input("Ingresa el número de ACL IPv4: "))

if acl <= 1 >= 99:
    print("Es una ACL Estándar.")
elif 100 <= acl:
    print("Es una ACL Extendida.")
else:
    print("❌ El número no corresponde a una ACL IPv4 válida.")
