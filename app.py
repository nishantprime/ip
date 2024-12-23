from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_ip():
    ip_route = request.headers.get("X-Forwarded-For")
    user_ip = ip_route.split(',')[0].strip()

    user_agent = str(request.user_agent)
    return user_ip + '\n\n' + user_agent

if __name__ == '__main__':
    app.run()
