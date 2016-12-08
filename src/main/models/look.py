import mongoengine as me 
from uuid import uuid4

class User(me.Document):
    
    user_id = me.StringField(default=uuid4().get_hex, unique=True)
    name = me.StringField()
    meta = {"indexes": ['user_id', 'name']}

class Book(me.Document):
    book_name = me.StringField()
    author_name = me.StringField()

