from mongoengine import Document, StringField

class Register(Document):
    username = StringField()
    password = StringField()
    dateOfBirth = StringField()
    email = StringField()
class Sound(Document):
    name = StringField()
    link = StringField()
    classIcon = StringField()
    subName = StringField()
