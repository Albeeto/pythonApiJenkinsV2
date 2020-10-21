from flask import Response, request
from database.models import Client
from flask_restful import Resource


class ClientsApi(Resource):
    def get(self):
        clients = Client.objects().to_json()
        return Response(clients, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        client = Client(**body).save()
        id = client.id
        return {'id': str(id)}, 200


class ClientApi(Resource):
    def put(self, id):
        body = request.get_json()
        Client.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        client = Client.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        try:
            client = Client.objects.get(id=id).to_json()
            return Response(client, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
