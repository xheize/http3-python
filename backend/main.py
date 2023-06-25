import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from app import app

server_config = Config()
server_config.insecure_bind = "127.0.0.1:80"
server_config.bind = "127.0.0.1:443"
server_config.quic_bind = "127.0.0.1:443"
server_config.certfile = "./cert.pem"
server_config.keyfile = "./key.pem"

asyncio.run(serve(app, server_config))
