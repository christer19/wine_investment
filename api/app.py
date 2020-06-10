from flask import Flask, jsonify, request
from service.models import Country, Region, Wine, database
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


regions_warp = {2: "Bordeaux Premier Cru - left bank", 3:"Bordeaux Margaux, France",
                5: "Bordeaux Pessac-Léognan/ Graves", 6: "Bordeaux St Emilion- right bank",
                7: "Bordeaux Pomerols - right bank"}

regions_wajs = {1: "Bordeaux Premier Cru - left bank"}

regions_walpb = {1: "Bordeaux Premier Cru - left bank", 2: "Bordeaux Pessac-Léognan/ Graves",
                 4: "Bordeaux St Emilion- right bank", 5: "Bordeaux Pomerols - right bank"}

regions_wanm = {1: "Bordeaux Premier Cru - left bank", 3: "Bordeaux Margaux", 4: "Bordeaux Pessac-Léognan/ Graves",
                5: "Bordeaux St Emilion- right bank", 6: "Bordeaux Pomerols - right bank"}

countries = {1: "France"}
countries_warp = {2: "France"

                  }
@app.route('/warp', methods=["GET"])
@cross_origin()
def warp_view(): #
    data = database(os.getenv('DATABASE_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_warp[wine.region_id],
                       "wine_country": countries_warp[wine.country_id]})
    return jsonify(output)

@app.route('/wanm', methods=["GET"])
@cross_origin()
def wanm_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_ONYX_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_wanm[wine.region_id],
                       "wine_country": countries[wine.country_id]})
    return jsonify(output)

@app.route('/walpb', methods=["GET"])
@cross_origin()
def walpb_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_COPPER_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_walpb[wine.region_id],
                       "wine_country": countries[wine.country_id]})
    return jsonify(output)

@app.route('/wajs', methods=["GET"])
@cross_origin()
def wajs_view():
    data = database(os.getenv('HEROKU_POSTGRESQL_BLUE_URL'))
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_wajs[wine.region_id],
                       "wine_country": countries[wine.country_id]})
    return jsonify(output)

if __name__ == '__main__':
    app.run(threaded=True, port=1337)
