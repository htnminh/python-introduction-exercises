from Address import Address
'''
class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
'''

class CampusAddress(Address):
    def __init__(self, office_number):
        Address.__init__(self, 'Dai Co Viet', '01')
        self.office_number = office_number

'''
obj = CampusAddress("B1")
print(obj.street_name, obj.number, obj.office_number)
print(isinstance(obj, Address), isinstance(obj, CampusAddress))
'''