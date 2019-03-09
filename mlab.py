import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds255005.mlab.com:55005/sound
host = "ds255005.mlab.com"
port = 55005
db_name = "sound"
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