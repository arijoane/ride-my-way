import unittest
from app import views
from run import app
import json

class Test_Viewing_Offers(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_get_available_offers(self):
        '''Test to fetch all offers'''
        response = self.app.post("/api/v1/add_ride",content_type='application/json',data=json.dumps(dict(driver="kyra",cartype="Raum",number_plate="UBA",destination="Kololo",mobile="0700000",fare=2000,pick="Ntinda"),))           
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/all_rides",content_type='application/json',data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"successfully fetched all offers")
        self.assertEquals("successfully fetched all offers","successfully fetched all offers")

    # def test_get_single_offer(self):
    #     '''Test to fetch single offer'''
    #     response = self.app.post("/api/v1/rides/add_offer",
    #         content_type='application/json',
    #         data=json.dumps(dict(id="1",driver_name="kyra",location="kawempe",
    #                             car_type="Benz",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
    #         ) 
    #     response = self.app.post("/api/v1/rides/add_offer",
    #         content_type='application/json',
    #         data=json.dumps(dict(id="2",driver_name="Natie",location="Wempes",
    #                             car_type="Benz",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
    #         )     
            
    #     reply = json.loads(response.data.decode())
    #     response2 = self.app.get("/api/v1/rides/2",
    #     content_type='application/json',
    #         data=reply)
    #     reply2 = json.loads(response2.data.decode())
    #     self.assertEquals(reply2["message"],"Successfully viewed single offer")
