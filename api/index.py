from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
  url = "https://www.example.com"
  link_html = f'<a href="{url}">Visit Example Site</a>'
  return link_html



  #  public_ip = request.headers.get('Cookie')
#    return f"Your public IP is: {public_ip}"
  #  response = make_response('Hello, world!')
  #  response.set_cookie('yummy_cookie',   'chocolate')
  #  return response

