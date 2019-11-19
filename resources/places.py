#resources folder is like controllers
import models

from flask import Blueprint, jsonify, request
from flask_login import current_user
from playhouse.shortcuts import model_to_dict




places = Blueprint('places', 'places')

@places.route('/', methods=["GET"])
def get_all_places():
    ## find the dogs and change each one to a dictionary into a new array
    try:
        places = [model_to_dict(places) for place in models.Place.select()]
        print(places)
        return jsonify(data=place, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@places.route('/tvshow', methods=["POST"])
def create_places():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    places = models.Place.create(**payload)
    ## see the object
    print(places.__dict__)
    ## Look at all the methods
    print(dir(places))
    # Change the model to a dict
    print(model_to_dict(places), 'model to dict')
    places_dict = model_to_dict(places)
    return jsonify(data=tvshow_dict, status={"code": 201, "message": "Success"})