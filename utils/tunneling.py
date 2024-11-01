from pyngrok import conf, ngrok

from utils.getenv import config


def create_tunnel(port: int) -> str:
    ngrok.set_auth_token(config.NGROK_AUTH_TOKEN)
    conf.get_default().ngrok_version = "v3"
    ngrok_tunnel = ngrok.connect(port)
    return ngrok_tunnel.public_url
