import os
import joblib
from flask import Flask,jsonify,request
import requests
import urllib.request
from bs4 import BeautifulSoup
from flask_restful import Api,Resource
from modeler.Modeler import Modeler
import metadata_parser

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        url = data['url']
        page = metadata_parser.MetadataParser(url=url)
        desc = page.get_metadatas('description')
        if(desc == None):
            desc = page.get_metadatas('description', strategy=['og',])
        if(desc == None):
            desc = page.get_metadatas('title')
        if(desc == None):
            desc = page.get_metadatas('title',strategy = ['og'])
        #todo - check data formats
        m = Modeler()
        if not os.path.isfile('models/webclass.joblib'):
            m.fit()
        prediction = m.predict(desc)
        return jsonify({
            'url':url,
            'Category':prediction[0]
        })
api.add_resource(Predict,'/predict')

if __name__ == '__main__':
    app.run(debug = True)



