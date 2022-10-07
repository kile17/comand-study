class Location:
    def __init__(self,name,mark,Location,iso,ipv4,mask,ipv6,user,password):
        self.name = name
        self.mark = mark
        self.Location = Location
        self.iso = iso
        self.ipv4 = ipv4
        self.mask = mask
        self.ipv6 = ipv6
        self.user = user
        self.password = password
    def myLocation(self):
        print("Nombre: " + self.name + " Marca: " + self.mark + " Ubicacion: " + self.Location + " IOS: " + self.iso + " IPV4: " + self.ipv4 + " Mask: " + self.mask + " IPV6: " + self.ipv6 + " USER: " + self.user + " PASSWORD: " + self.password + ".")

loc1 = Location("R1,","Cisco,","Conectado a ISP Y a R2,","C2900-UNIVERSALK9-M,","200.100.100.1 - 192.168.1.1","255.255.255.252","2001:db8:acad:1::1/64","adminR1","Cisco123")
loc1.myLocation()
loc2 = Location("R2,","Cisco,","Conectado a R1,","C1841-ADVIPSERVICESK9-M","192.168.1.2","255.255.255.252","2001:db8:acad:3::1/64","adminR2","Cisco123")
loc2.myLocation()
loc3 = Location("ISP,","Cisco,","Conectado a R1,","C1900-UNIVERSALK9-M","200.100.100.2","255.255.255.252","2001:db8:acad:2::1/64","admin","Cisco123")
loc3.myLocation()
