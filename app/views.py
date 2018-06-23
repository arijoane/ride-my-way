from app import app
from app.model import RideOffer, Passenger, Driver
from flask import request, Flask, json, jsonify

rides = { }

@app.route("/api/v1/rides", methods=['GET'])
def get_rides():
    pass

@app.route("/api/v1/rides/<int:ride_id>",methods=['GET'])
def get_single_ride():
    pass


@app.route("/api/v1/rides", methods=['POST'])
def create_ride():
    pass

@app.route("/api/v1/rides/<int:ride_id>/requests", methods=['POST'])
def join_ride():
    pass

