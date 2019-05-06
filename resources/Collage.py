from flask import request
from flask_restful import Resource
from Model import db, Collage, CollageSchema

collages_schema = CollageSchema(many=True)
collage_schema = CollageSchema()

class CollageResource(Resource):
    def get(self):
        collages = Collage.query.all()
        collages = collages_schema.dump(collages).data
        return {'status': 'success', 'data': collages}, 200

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 100
        data, errors = collage_schema.load(json_data)

        if errors:
            return errors, 422
        collage = Collage.query.filter_by(name=data['name']).first()

        if collage:
            return {'message': 'Biodata already exists'}, 400
        collage = Collage(
            name=json_data['name']
        )

        db.session.add(collage)
        db.session.commit()

        result = collage_schema.dump(collage).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = collage_schema.load(json_data)
        if errors:
            return errors, 422
        biodata = Collage.query.filter_by(id=data['id']).first()
        if not biodata:
            return {'message': 'Category does not exist'}, 400
        biodata.name = data['name']
        db.session.commit()

        result = collage_schema.dump(biodata).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = collage_schema.load(json_data)
        if errors:
            return errors, 422
        biodata = Collage.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = collage_schema.dump(biodata).data

        return {"status": 'success', 'data': result}, 204

class CollageResources(Resource):
    def get(self,id):
        collages = Collage.query.filter_by(id = id)
        collages = collages_schema.dump(collages).data
        return {'status': 'success', 'data': collages}, 200




