from flask import Flask, request, jsonify, make_response, render_template
from flask_restplus import Api, Resource
import pandas as pd

flask_app = Flask(__name__)
app = Api(app=flask_app,
          version="1.0",
          title="Iris Plant identifier",
          description="Predict the type of iris plant")

name_space = app.namespace('datapage', description='Df APIs')

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

@name_space.route("/")
class MainClass(Resource):

    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

    # @app.expect(model)
    def post(self):
        try:
            teamsString = request.json
            response = jsonify({
                "statusCode": 200,
                "status": "Prediction made",
                "result": teamsString
                # "result": df.to_json(orient='split')
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as error:
            return jsonify({
                "statusCode": 500,
                "status": "Could not make prediction",
                "error": str(error)
            })
