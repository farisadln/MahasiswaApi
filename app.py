from flask import Blueprint
from flask_restful import Api
from resources.Biodata import BiodataResource
from resources.Collage import CollageResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(BiodataResource, '/Biodata')
api.add_resource(CollageResource, '/Collage')