import os
from flask_cors import CORS, cross_origin
from app import create_app

# reading this from config file
config_name = "development"
demo = create_app(config_name)
#print(demo.DEBUG)
#CORS(app)
if __name__ == '__main__':
    app = create_app(config_name)
    app.run(debug = True)