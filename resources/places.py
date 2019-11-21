#resources folder is like controllers
import models

from flask import Blueprint, jsonify, request
# from flask_login import current_user
from playhouse.shortcuts import model_to_dict




place = Blueprint('places', 'place')

@place.route('/', methods=["GET"])
def get_all_places():
    ## find the dogs and change each one to a dictionary into a new array
    try:
        places = [model_to_dict(place) for place in models.Place.select()]
        print(places)
        return jsonify(data=places, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@place.route('/', methods=["POST"])
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
    return jsonify(data=places_dict, status={"code": 201, "message": "Success"})



@place.route('/<id>', methods=["GET"])
def get_one_places(id):
    print(id, 'reserved word?')
    place = models.Place.get_by_id(id)
    print(places.__dict__)
    return jsonify(data=model_to_dict(places), status={"code": 200, "message": "Success"})



@place.route('/<id>', methods=["PUT"])
def update_places(id):
    payload = request.get_json()
    query = models.Place.update(**payload).where(models.Place.id==id)
    query.execute() # you have to execute the update queries
    return jsonify(data=model_to_dict(models.Place.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})



@place.route('/<id>', methods=["Delete"])
def delete_places(id):
    query = models.Place.delete().where(models.Place.id==id)
    query.execute() # you have to execute the update queries
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})





# @places.route('/<id>/', methods=["DELETE"])
# def delete_places(id):
#     places_to_delete = models.Place.get(id=id)
#     # TODO: put above line in try catch where catch returns 404 because id of dog is invalid
#     if not current_user.is_authenticated: # Checks if user is logged in
#         return jsonify(data={}, status={'code': 401, 'message': 'You must be logged in to create a dog'})
#     if places_to_delete.owner.id is not current_user.id: 
#         # Checks if owner (User) of dog has the same id as the logged in User
#         # If the ids don't match send 401 - unauthorized back to user
#         return jsonify(data={}, status={'code': 401, 'message': 'You can only delete dog you own'})
    
#     # Delete the dog and send success response back to user
#     places_to_delete.delete()
#     return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})

# @places.route('/<places_id>/', methods=['PATCH'])
# def update_places(place_id):
#     new_places_data = request.get_json()

#     updated_places = models.Place.update(
#         city=new_places_data['city'],
#         country=new_places_data['country'],
#         text=new_places_data['text']
#         image=new_places_data['image']
#     ).where(models.Place.id==places_id).execute()
#     update_places_dict = model_to_dict(models.Place.get(id=place_id))
#     return jsonify(status={'code': 200, 'msg': 'success'}, data=update_dog_dict)









