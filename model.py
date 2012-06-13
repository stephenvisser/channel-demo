from google.appengine.ext import ndb

class Connection(ndb.Model):
  created = ndb.DateTimeProperty(auto_now_add=True)
  info = ndb.StringProperty()
  changed = ndb.DateTimeProperty(auto_now=True)
  connected = ndb.BooleanProperty()

