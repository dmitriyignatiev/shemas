from aiohttp import web
from routes import setup_routes, init_routes
from db import init_pg, close_pg
from settings import config
import aiohttp_cors

app = web.Application()
cors = aiohttp_cors.setup(app)

init_routes(app, cors)
setup_routes(app)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app, port=8085)
