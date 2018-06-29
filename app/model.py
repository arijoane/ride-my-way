

"""a class representing the Passenger model"""
class Passenger:
    counter =1
    def __init__(self,name,username,email,contact,country,password,confirm_password):
        self.name = name
        self.username = username
        self.email = email
        self.contact = contact
        self.country = country
        self.password = password
        self.confirm_password = confirm_password
        self.id = self.counter
        self.counter +=1

    

class Driver:
    """A class representing the Driver Model"""
    counter =1
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
        self.id = Driver.counter
        Driver.counter +=1

    

        

class RideOffer:
    """A class representing the Ride_offer model"""
    counter =1
    def __init__(self,driver,cartype,number_plate,destination,fare,mobile,pick):
        self.driver = driver 
        self.cartype = cartype
        self.number_plate = number_plate
        self.mobile = mobile
        self.destination = destination
        self.fare = fare 
        self.pick = pick
        self.id = RideOffer.counter
        RideOffer.counter +=1

class request:
    """A class representing the requests model"""
    counter =1
    def __init__(self,PName,contact,place):
        self.PName = PName
        self.contact = contact
        self.place = place
        self.id = request.counter
        request.counter +=1
    


