#Determine if proper ip address

def properIp(address):
    x = address.split(".")
    x = [int(i) for i in x]
    for i in x:
        if(i < 0 or i > 255):
            return False
    return True


address = "192.168.1.255"
print(properIp(address))