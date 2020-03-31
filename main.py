
def main():
    octal_equivalents = [256,128,64,32,16,8,4,2,1]
    ip_blocks = 4
    no_of_host = 254
    network_id = "192.168.10.10"
    broadcast_ip = "192.168.10.10"
    first_ip = "192.168.10.10"
    last_ip = "192.168.10.2"
    subnet_mask = "255.255.255.254"

    ip_address = input("IP Address:")
    cidrs = list(map(int, input("CIDR/s: ").split()))

    print("IP Address: ",ip_address)
    print("CIDRs: ", cidrs)

    print(convert_ip_to_binary(ip_address))
    
    
    # for cidr in cidrs:

    #     # e.g 24
    #     # so 24 "1" bits are turned on
    #     # on the given ip address
    #     # for index in range(0,ip_blocks):
    #     #     print(sum(octal_equivalents[0:int(cidr)]))

        

    #     print("CIDR:", cidr )
    #     print("No. of hosts:", no_of_host)
    #     print("Subnet:", subnet_mask)
    #     print("Network ID:",network_id)
    #     print("Broadcast IP:",broadcast_ip)
    #     print("First IP:",first_ip)
    #     print("Last IP:",last_ip)

def convert_ip_to_binary(ip_address):

    octal_equivalents = [128, 64, 32, 16, 8, 4, 2, 1]

    for octet in ip_address.split("."):

        value = int(octet)

        for x in octal_equivalents:
            
            for y in octal_equivalents:

                if x + y > int(octet):
                    continue
                if x + y <= int(octet):
                    value = x + y
        
        print("value is : " ,value)


       

        # while dividend > divisor:
            
        #     result = divmod(dividend, divisor)
        #     quotient = result[0]
        #     print("quotient:", quotient)
        #     print("remainder:", result[1])
        #     remainder.insert(0,result[1])

        #     if int(quotient) == 0:
        #         # do the final division and break the loop
        #         divmod(dividend, divisor)
        #         remainder.insert(0, result[1])
        #         break

        #     dividend = quotient
        
        print("Remainder for octet " + octet  + ":", remainder)
        
    return ip_address


main()
