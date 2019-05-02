from flask import request
from flask_restful import Resource
from Model import db, Biodata, Collage, BiodataSchema

biodatas_schema = BiodataSchema(many=True)
biodata_schema = BiodataSchema()

class BiodataResource(Resource):
    def get(self):
        biodatas = Biodata.query.all()
        biodatas = biodatas_schema.dump(biodatas).data
        return {"status": "success", "data": biodatas}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = biodata_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        collage_id = Collage.query.filter_by(id=data['collage_id']).first()
        if not collage_id:
            return {'status': 'error', 'message': 'comment category not found'}, 400
        biodata = Biodata(
            collage_id=data['collage_id'],
            nim=json_data['nim'],
            name=json_data['name']
        )
        db.session.add(biodata)
        db.session.commit()

        result = biodata_schema.dump(biodata).data

        return {'status': "success", 'data': result}, 201
