from aiohttp import web

async def handle(request):
    return web.Response(text="Bot is running!")

async def health_check(request):
    return web.Response(text="OK", status=200)

async def web_server():
    app = web.Application()
    app.router.add_get("/", handle)  # Homepage
    app.router.add_get("/health", health_check)  # Health check route for Koyeb
    return app
