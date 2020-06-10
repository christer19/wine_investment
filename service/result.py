from service.parser import parser_main
from service.parse_excel import get_wines_set
import time
import requests


def get_min_max_years(wines_list):
    years = []
    for year in wines_list:
        years.append(year['year'])
    return min(years), max(years)


# def get_price(wine_name, year):
#     url = f"https://api.wine-searcher.com/x?api_key=test6ws202005&winename={wine_name}&vintage={year}&format=J"
#     r = requests.get(url)
#     json_result = r.json()['wine-details'][0]['price-average']
#     return float(json_result)

def get_price(wine_name, year):
    return 0

def scores_dict(wines_list):
    scores = {}
    for wine in wines_list:
        if scores.get(wine['critic'], 0):
            if scores[wine['critic']].get(wine['score']):
                scores[wine['critic']][wine['score']].append(wine['year'])
            else:
                scores[wine['critic']][wine['score']] = [wine['year']]
            # scores[wine['critic']][wine['score']].append(wine['year'])
        else:
            scores[wine['critic']] = {wine['score']:[wine['year']]}
    # scores['colour'] = [i['colour'] for i in wines_list[1]][0]
    # scores['region'] = [i['region'] for i in wines_list[1]][0]
    # scores['grape'] = [i['grape'] for i in wines_list[1]][0]
    return scores

def calculate_yearly_diff(wine_name):
    parser_result =  parser_main(wine_name)
    scores = scores_dict(parser_result[0])
    etc = parser_result[1]
    arr = []
    for critic in scores.keys():
        for score in scores[critic]:
            if len(scores[critic][score]) > 1:
                # if we have more than 1 wine for a specific score we take
                # latest and earliest dates and find the year difference between them
                price_latest = get_price(wine_name, scores[critic][score][0])
                price_earliest = get_price(wine_name, scores[critic][score][-1])
                years_diff = int(scores[critic][score][0]) - int(scores[critic][score][-1])
                sum_price = None #sum((float(price_earliest), float(price_latest)))
                diff = None #sum_price // years_diff
                arr.append(
                    {
                    "name": wine_name,
                    "Colour": [i['colour'] for i in etc][0],
                    "Grape": [i['grape'] for i in etc][0],
                    "Region": [i['region'] for i in etc][0],
                    "Vintage" : int(scores[critic][score][0]),
                    "Quantity": None,
                    "Price": None,#price_latest,
                    "Critic": critic,
                    "Years": years_diff,
                    "Vs Vintage": int(scores[critic][score][-1]),
                    "Quantity": None,
                    "Price difference":  None, #price_latest - price_earliest,
                    "increase per year": None, #(price_latest - price_earliest) // years_diff,
                    "increase per year %": None#(1 - (price_earliest - price_latest)) * 100
                    }
                    )
    return arr

def parse_all_excel_wines():
    result = []
    for wine in get_wines_set():
        result.extend(calculate_yearly_diff(wine))
        time.sleep(20)
    return result

# if __name__ == '__main__':
#   print(calculate_yearly_diff())

# def kill_chrome():
#   import os
#   os.system("kill $(ps aux | grep Chrome | grep -v grep | awk '{print $2}')")
    # os.system("pkill -9 Google Chrome Helper")

