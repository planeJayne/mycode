#!/usr/bin/env python3

#create a list containing three items
my_list = ["192.168.0.0", 5060, "up"]

#display first item in list
print("The first item in the list (IP): " + my_list[0])

#display second item in list
print("The second item in the list(port): " + str( my_list[1]))

#display the third item in the list
print("The last item in the list (state) :" + my_list[2])

iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1","ssh"]

#print only ip addresses
print("The IP addresses given are :" + str(iplist[3][4]))
