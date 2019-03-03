import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds113815.mlab.com:13815/c4e25-web
host = "ds113815.mlab.com"
port = 13815
db_name = "c4e25-web"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())