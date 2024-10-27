from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://casablanca-s78l.vercel.app/"
    link_html = f'<a href="{url}">Visit Example Site</a>'

    # Create the response with the link HTML
    response = make_response(link_html)
    
    # Set the cookie
    response.set_cookie('hamza', 'one', samesite='None', secure=True)
    
    return response


  #  public_ip = request.headers.get('Cookie')
#    return f"Your public IP is: {public_ip}"
  #  response = make_response('Hello, world!')
  #  response.set_cookie('yummy_cookie',   'chocolate')
  #  return response

