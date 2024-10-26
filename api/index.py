from flask import Flask, request, make_response, render_template


app = Flask(__name__)

@app.route('/')
def get_public_ip():
    # The 'X-Forwarded-For' header contains the public IP of the requester
    public_ip = request.headers.get('Cookie')
    return f"Your public IP is: {public_ip}"




