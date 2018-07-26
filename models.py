from google.appengine.ext import ndb

class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    college = ndb.StringProperty()

class Advice(ndb.Model):
    book_name = ndb.StringProperty()
    author_name = ndb.StringProperty()
    
