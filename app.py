from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def get_ip():
    client_ip = request.headers.get('X-Envoy-Downstream-Service-Cluster')
    if client_ip is None:
        client_ip = request.remote_addr
    server_ip = socket.gethostbyname(socket.gethostname())
    return f"Client IP: {client_ip}\nServer IP: {server_ip}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

