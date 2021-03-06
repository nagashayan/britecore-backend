from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()
print(app_config["development"])
def create_app(config_name):
    from .models import FeatureDetails

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
            client_priority = str(request.data.get('client_priority', ''))
            if title:
                feature = FeatureDetails(client_id, title, description, target_date, product_area, client_priority)
                #check if the client already exists with same priority if yes then reorder
                feature.checkPriorityOrder()
                feature.save()
                response = jsonify({
                'id': feature.id,     
                'client_id': feature.client_id,
                'client_priority': feature.client_priority,
                'title': feature.title,
                'description': feature.description,
                'target_date': feature.target_date,
                'product_area': feature.product_area,
                'date_created': feature.date_created,
                'date_modified': feature.date_modified
            })
                response.status_code = 201
                return response
        else:
            # GET All
            features = FeatureDetails.get_all()
            results = []

            for feature in features:
                obj ={
                'id': feature.id,
                'client_id': feature.client_id,
                'client_priority': feature.client_priority,
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

    @app.route('/feature/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def feature_manipulation(id, **kwargs):
     # retrieve a featurelist using it's ID
        feature = FeatureDetails.query.filter_by(id=id).first()
        if not feature:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            feature.delete()
            return {
            "message": "feature {} deleted successfully".format(feature.id) 
         }, 200

        elif request.method == 'PUT':

            feature.title = str(request.data.get('title', ''))
            feature.description = str(request.data.get('description', ''))
            feature.target_date = str(request.data.get('target_date', ''))
            feature.product_area = str(request.data.get('product_area', ''))
            
            feature.save()
            
            response = jsonify({
                'id': feature.id,
                'client_id': feature.client_id,
                'client_priority': feature.client_priority,
                'title': feature.title,
                'description': feature.description,
                'target_date': feature.target_date,
                'product_area': feature.product_area,
                'date_created': feature.date_created,
                'date_modified': feature.date_modified
            })
            response.status_code = 200
            return response

        else:
        # GET
            response = jsonify({
                'id': feature.id,
                'client_id': feature.client_id,
                'client_priority': feature.client_priority,
                'title': feature.title,
                'description': feature.description,
                'target_date': feature.target_date,
                'product_area': feature.product_area,
                'date_created': feature.date_created,
                'date_modified': feature.date_modified
            })
            response.status_code = 200
            return response

    return app


    