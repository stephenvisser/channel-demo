from google.appengine.ext import ndb

class Connection(ndb.Model):
  opened = ndb.DateTimeProperty(auto_now_add=True)
  info = ndb.StringProperty()
  changed = ndb.DateTimeProperty(auto_now=True)
  status = ndb.StringProperty()

