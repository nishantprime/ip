from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_ip():
    ip_route = request.headers.get("X-Forwarded-For")
    user_ip = ip_route.split(',')[0].strip()

    user = request.user_agent
    return user_ip + str(user)

if __name__ == '__main__':
    app.run()
