from pymongo import MongoClient
from service.result import parse_all_excel_wines
client = MongoClient('localhost', 27017)

db = client['wines']
wines = db.wines
wine = wines.segment.insert_many(parse_all_excel_wines())


