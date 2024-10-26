from flask import Flask, request, make_response, render_template
import webbrowser


app = Flask(__name__)


@app.route('/')
def home():
    url = "https://www.example.com"
    webbrowser.open(url)

  #  public_ip = request.headers.get('Cookie')
#    return f"Your public IP is: {public_ip}"
  #  response = make_response('Hello, world!')
  #  response.set_cookie('yummy_cookie',   'chocolate')
  #  return response

