from flask import Flask, jsonify, request
from service.models import Country, Region, Wine, database
app = Flask(__name__)

regions_warp = {2: "Bordeaux Premier Cru - left bank", 3:"Bordeaux Margaux, France",
                5: "Bordeaux Pessac-Léognan/ Graves", 6: "Bordeaux St Emilion- right bank",
                7: "Bordeaux Pomerols - right bank"}

regions_wanm = {}
@app.route('/warp', methods=["GET"])
def warp_view():
    data = database('postgres://zlilcflfplhrlz:6f30e004db1d1350f142c7b5d1d08a265be214a772c6adf88439c8242e434dfd@ \
                    ec2-54-247-89-181.eu-west-1.compute.amazonaws.com:5432/dcq1n63u85c8ce')
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": regions_warp[wine.region_id],
                       "wine_country": regions_warp[wine.country_id]})
    return jsonify(output)

@app.route('/wanm', methods=["GET"])
def wanm_view():
    data = database('postgres://tcnaxsfrvvjubs:378045f5bb41b0c42e02e0304acab0ed6050e592ef716d599ad74b9f312abc53@ \
                    ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/d4a36gtnkmqcis')
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

@app.route('/walpb', methods=["GET"])
def walpb_view():
    data = database('postgres://vuwtbfbuqhtbwo:2ef525992f1ed61fef6591c34fe1e646f47182be56b485a23f0af6efa2019550@ \
                    ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/d2dblv80gg5951')
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

@app.route('/wajs', methods=["GET"])
def wajs_view():
    data = database('postgres://axguhrtagziiaq:9dc31414d35bea7e9d6d2667665dbf5b32727f50c17e52fcda6bdfe038e533ce@ \
                    ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/d62m4t98j79fs5')
    output = []
    for wine in data.query(Wine):
        output.append({"wine_name": wine.name,
                       "wine_year": wine.year,
                       "wine_region": [wine.region_id],
                       "wine_country": [wine.country_id]})
    return jsonify(output)

if __name__ == '__main__':
    app.run(threaded=True, port=1337)
