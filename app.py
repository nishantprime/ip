from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_ip():
    ip_route = request.headers.get("X-Forwarded-For")
    user_ip = ip_route.split(',')[0].strip()
    return f"Your IP Addresss is {user_ip} \n\nAnd IP Route is {ip_route}"

if __name__ == '__main__':
    app.run()
