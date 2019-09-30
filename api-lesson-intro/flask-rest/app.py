from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of a guest')
parser.add_argument('id', type=int, help='Numerical ID of a guest in the list')

# A list containing names of guests
guest_list = ['Akansh', 'Bill Gates', 'Elon Musk']


# GET request to read all items in our list
class GuestList(Resource):
    def get(self):
        return {'names': [name for name in guest_list]}, 200


# GET request to check for a specific guest
class GuestById(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']

        return {'name': guest_list[id]}


# POST request to create a new guest into our list
class GuestAdd(Resource):
    def post(self):
        args = parser.parse_args()
        name = args['name']

        guest_list.append(name)
        return {'message': 'Guest added'}


# POST request to delete a name from our list
class GuestDelete(Resource):
    def post(self):
        args = parser.parse_args()
        id = args['id']

        guest_list.pop(id)
        return {'message': 'Guest removed'}


# POST request to update an existing guest in our list
class GuestUpdate(Resource):
    def put(self):
        args = parser.parse_args()
        id = args['id']
        name = args['name']

        guest_list[id] = name
        return {'message': 'Guest updated'}


# Creating endpoints for our API
api.add_resource(GuestList, '/guests')
api.add_resource(GuestById, '/guest')
api.add_resource(GuestAdd, '/guest/add')
api.add_resource(GuestDelete, '/guest/delete')
api.add_resource(GuestUpdate, '/guest/update')


if __name__ == '__main__':
    app.run()
