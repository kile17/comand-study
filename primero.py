import ipaddress
Id_Red=input("Entre la direccion de red y Prefijo:")
ip=ipaddress.IPv4Network(Id_Red)
print("La mascara de sub red es:",ip.netmask)
