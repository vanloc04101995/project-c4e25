from mongoengine import Document, StringField

class Register(Document):
    username = StringField()
    password = StringField()
    dateOfBirth = StringField()
    email = StringField()
<<<<<<< HEAD
    
class Sound(Document):
    name = StringField()
    classIcon = StringField()
    link = StringField()
    
=======
class Sound(Document):
    name = StringField()
    link = StringField()
    classIcon = StringField()

>>>>>>> fb48189a7147537326dd5254b54db7efa9f0e664
