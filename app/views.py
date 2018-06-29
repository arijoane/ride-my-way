from app import app
from app.model import RideOffer, Passenger, Driver
from flask import request, Flask, json, jsonify

driver_list = []
passenger_list = []
ride_offer_list = []

@app.route("/api/v1/drivers", methods=['GET','POST'])
def drivers():
    if request.method == 'GET':
        return jsonify({'drivers':driver_list})
    
    if request.method == 'POST':
        params = request.get_json()
        driver = Driver(params['name'],params['username'],params['email'],params['contact'],params['country'],params['password'],params['confirm_password'],params['licence_number'],params['number_plate'])
        driver_list.append(driver.__dict__)
        return jsonify({'driver':driver.__dict__})
        
@app.route("/api/v1/passengers",methods=['GET','POST'])
def passengers():
    if request.method == 'GET':
        return jsonify({'passengers': passenger_list})

    if request.method == 'POST':
        params  = request.get_json()
        passenger = Passenger(params['name'],params['username'],params['email'],params['contact'],params['country'],params['password'],params['confirm_password'])
        passenger_list.append(passenger.__dict__)
        return jsonify({'passenger':passenger.__dict__})

@app.route("/api/v1/all_rides", methods=['GET'])

def ride_offer():
    if request.method == 'GET':
        return jsonify({'ride_offer':ride_offer_list,'message':'successfully fetched all offers'})
        

@app.route("/api/v1/add_ride", methods=['POST'])
def create_offer():
    if request.method == 'POST':
        box = request.get_json()
        offer = RideOffer(box['driver'], box['cartype'],box['number_plate'],box['destination'],box['fare'],box['mobile'],box['pick'])
        ride_offer_list.append(offer.__dict__)
        #return jsonify({'ride_offer':offer.__dict__})

        return jsonify ({'message':'successfully created','ride_offer':offer.__dict__}), 201

    

@app.route("/api/v1/rides/<int:ride_id>",methods=['GET'])
def get_single_ride(ride_id):
    if request.method  == 'GET':
        for item in ride_offer_list:
            if item['id'] == ride_id:
                return jsonify({'ride':item})
                
        return jsonify({'error':'ride not found'})
    

@app.route("/api/v1/")

    
