from views import index
from api.api_views import gqil_view, gql_view
import aiohttp_cors


def setup_routes(app):
    app.router.add_get('/', index)
    
def init_routes(app, cors):
    app.router.add_route('*', '/graphiql', gqil_view, name='graphiql')

    resource = cors.add(app.router.add_resource("/graphql"), {
        "*": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
            allow_credentials=True,
            allow_methods=["POST", "PUT", "GET"]),
    })
    resource.add_route("POST", gql_view)
    resource.add_route("PUT", gql_view)
    resource.add_route("GET", gql_view)