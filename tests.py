import unittest
from app.model import RideOffer, Passenger, Driver
from run import app

class TestRidemyway(unittest.TestCase):

    def create_app(self):
        return app

    def test_it_creates_ride(self):
        """test that allows a driver to create a ride"""
        offer = RideOffer('Shab','Raum','UBA','kololo','2000','0700000','Ntinda')
        self.assertEqual(offer.driver,"Shab")
        self.assertEqual(offer.cartype,"Raum")
        self.assertEqual(offer.number_plate,"UBA")
        self.assertEqual(offer.mobile,"0700000")
        self.assertEqual(offer.destination,"kololo")
        self.assertEqual(offer.fare,'2000')
        self.assertEqual(offer.pick,"Ntinda")

#def test_it_lists_all_ride_Offers(self):
       # """test that shows all ride offers"""