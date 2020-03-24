#Print Address for a specified format -("House Number" "Street Name")
def format_address(address):
        lis=address.split()
        addr=""
        for i in lis:
            if i.isnumeric():
                hno=i
            elif i.isalpha():
                addr=addr+' '+i
        return "House number {} on street named{}".format(hno,addr)
print(format_address("123 Main Street"))