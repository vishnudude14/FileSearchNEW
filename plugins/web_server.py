from aiohttp import web
from plugins.route import routes

async def web_server():
    app = web.Application()
    app.add_routes(routes)
    return app
