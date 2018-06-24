

"""a class representing the Passenger model"""
class Passenger:
    def __init__(self,name,username,email,contact,country,password,confirm_password):
        self.name = name
        self.username = username
        self.email = email
        self.contact = contact
        self.country = country
        self.password = password
        self.confirm_password = confirm_password

    

class Driver:
    """A class representing the Driver Model"""
    def __init__(self, name,username,email,contact,country,password,confirm_password,licence_number,number_plate):      
        self.name = name
        self.username = username
        self.email = email
        self.contact = contact
        self.country = country
        self.password = password
        self.confirm_password = confirm_password
        self.licence_number = licence_number
        self.number_plate = number_plate

    

        

class RideOffer:
    """A class representing the Ride_offer model"""
    def __init__(self,driver,cartype,number_plate,destination,fare,mobile,pick):
        self.driver = driver 
        self.cartype = cartype
        self.number_plate = number_plate
        self.mobile = mobile
        self.destination = destination
        self.fare = fare 
        self.pick = pick

    


