
from terminaltables import AsciiTable

octal_equivalents = [128, 64, 32, 16, 8, 4, 2, 1]
ip_blocks = 4

def main():
       
    no_of_host = 254
    network_id = "192.168.10.10"
    broadcast_ip = "192.168.10.10"
    first_ip = "192.168.10.10"
    last_ip = "192.168.10.2"
    subnet_mask = "255.255.255.254"

    ip_address = input("IP Address with CIDR (e.g 192.168.10.10/24):")
    cidr = ip_address.split("/")[1]

    # identify the subnet mask
    # e.g 24
    # so 24 "1" bits are turned on
    # on the given ip address

    # first is to convert the CIDR into its binary representation
    subnet_mask = cidr_to_binary(int(cidr))

    table_data = [
        ['I.P ADDRESS', ip_address],
        ['CIDR', '/' + cidr ],
        ['Subnet Mask', subnet_mask],
        ['Network ID ', '192.168.2.142'],
        ['Broadcast ID ', '192.168.2.142'],
        ['First I.P', '192.168.2.142'],
        ['Last I.P ', '192.168.2.142']
    ]

    table = AsciiTable(table_data,None)
    print("SUBNET TABLE FOR ",ip_address)
    print(table.table)

def cidr_to_binary(cidr):
    subnet_binary = []
    subnet_octets = []
    
    # turn on the "1" bits based on the cidr
    subnet_binary[0:cidr] = [1] * cidr
    # turn on the "0" bits after the cidr range
    subnet_binary[cidr:32] = [0] * cidr
    subnet_octets.append(subnet_binary[0:8])
    subnet_octets.append(subnet_binary[8:16])
    subnet_octets.append(subnet_binary[16:24])
    subnet_octets.append(subnet_binary[24:32])

    # print(subnet_octets)
    # print(second_octet)
    # print(third_octet)
    # print(fourth_octet)

    # get the subnet mask
    subnet_mask = ''
    for x in range(len(subnet_octets)):
        temp_sum = 0
        for i in range(0,8):
            if subnet_octets[x][i] > 0:
                temp_sum += octal_equivalents[i]
        subnet_mask += str(temp_sum) + "."

    return subnet_mask

main()

    # cidrs = list(map(int, input("CIDR/s: ").split()))

    # print("IP Address: ",ip_address)
    # print("CIDRs: ", cidrs)

    # print(convert_ip_to_binary(ip_address))
    
    
    # for cidr in cidrs:

    #     # e.g 24
    #     # so 24 "1" bits are turned on
    #     # on the given ip addressr5
    #     # for index in range(0,ip_blocks):
    #     #     print(sum(octal_equivalents[0:int(cidr)]))

        

    #     print("CIDR:", cidr )
    #     print("No. of hosts:", no_of_host)
    #     print("Subnet:", subnet_mask)
    #     print("Network ID:",network_id)
    #     print("Broadcast IP:",broadcast_ip)
    #     print("First IP:",first_ip)
    #     print("Last IP:",last_ip)

# def convert_ip_to_binary(ip_address):

    # octal_equivalents = [128, 64, 32, 16, 8, 4, 2, 1]
    # octets = ip_address.split(".")
    # x = 0
    # binary_equivalent = []

    # for i in range(len(octets)):
    #     if int(octets) > octal_equivalents[i]:
    #     for y in range(0,8):

    #         temp = octal_equivalents[y] + octal_equivalents[y+1]

    #         if temp == int(octets[i]):

    #         if temp < int(octets[i]):
    #             y+= 1

       

        # for x in octal_equivalents:
            
        #     for y in octal_equivalents:

        #         if x + y > int(octet):
        #             continue
        #         if x + y <= int(octet):
        #             value = x + y
        
        # print("value is : " ,value)


       

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
        
        # print("Remainder for octet " + octet  + ":", remainder)
        # return ip_addres

