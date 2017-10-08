from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from models import FeatureDetails

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #adding create functionality
    @app.route('/feature/', methods=['POST', 'GET'])
    def feature():
        if request.method == "POST":
            client_id = str(request.data.get('client_id', ''))
            title = str(request.data.get('title', ''))
            description = str(request.data.get('description', ''))
            target_date = str(request.data.get('target_date', ''))
            product_area = str(request.data.get('product_area', ''))
            if title:
                feature = FeatureDetails(client_id, title, description, target_date, product_area)
                feature.save()
                response = jsonify({
                    'client_id': feature.client_id,
                    'title': feature.title,
                    'description': feature.description,
                    'target_date': feature.target_date,
                    'product_area' : feature.product_area,
                    'date_created': feature.date_created,
                    'date_modified': feature.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            features = FeatureDetails.get_all()
            results = []

            for feature in features:
                obj = {
                    'client_id': feature.client_id,
                    'title': feature.title,
                    'description': feature.description,
                    'target_date': feature.target_date,
                    'product_area': feature.product_area,
                    'date_created': feature.date_created,
                    'date_modified': feature.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app