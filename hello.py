import os

from app import create_app
# reading this from config file
config_name = "development"
app = create_app(config_name)

#keeping it still, so that test wont fail
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()