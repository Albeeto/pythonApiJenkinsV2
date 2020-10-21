from .client import ClientsApi, ClientApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')
