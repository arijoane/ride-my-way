from app import app
from app.model import RideOffer, Passenger, Driver
from flask import request, Flask, json, jsonify

rides = { }

@app.route("/api/v1/rides", methods=['GET'])
def get_rides():
    pass

@app.route("/api/v1/rides/get>",method=['GET'])
def get_single_ride():
    pass


@app.route("/api/v1/rides/create", methods=['POST'])
def create_ride():
    pass

@app.route("/api/v1/rides/join", methods=['POST'])
def join_ride():
    pass

"""
@app.route("/api/v1/createride", methods=['GET','POST'])
def create_ride():
    # creates a ride_offer
    if 

    

@app.route("/rides", methods=['GET'])
def ride_offers():
    # fetches all ride offers 
    if request.method == 'GET':
        return ride, 200



@app.route("/rideId>",method=['GET'])
def single_ride_offer():
    # fetches a single ride_offer from the ride_-offer list
    if request.method == 'GET':
        ride_offers  = ride_offers.query.get(id=id)
        return{"message":"succeeded" },200
"""