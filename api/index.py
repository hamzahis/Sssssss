from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

@app.route('/')
def set_cookie():
    url = "https://casablanca-s78l.vercel.app/"
    link_html = f'<a href="{url}">Visit Example Site</a>'
    
    # Create the response with the link HTML
    response = make_response(link_html)
    
    # Set a cookie that can be accessed by the third-party
    response.set_cookie('user_data', 'hamza', samesite='None', secure=True)
    
    return response

@app.route('/get-cookie')
def get_cookie():
    # This endpoint allows a third-party site to access the cookie value
    user_data = request.cookies.get('user_data')
    if user_data:
        return jsonify({"user_data": user_data})
    else:
        return jsonify({"error": "No user data found"}), 404

if __name__ == "__main__":
    app.run(debug=True)









"""
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'first_visit' not in request.cookies:
        resp = make_response(render_template('index.html'))
        resp.set_cookie('first_visit', 'true')  # 30 days
        return resp
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
"""









"""

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
"""

  #  public_ip = request.headers.get('Cookie')
#    return f"Your public IP is: {public_ip}"
  #  response = make_response('Hello, world!')
  #  response.set_cookie('yummy_cookie',   'chocolate')
  #  return response

