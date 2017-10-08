import os
from flask_cors import CORS, cross_origin
from app import create_app

# reading this from config file
config_name = "development"
app = create_app(config_name)
CORS(app)

if __name__ == '__main__':
    app.run()