#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
from model import Connection
from webapp2_extras import jinja2
from google.appengine.api import channel

class ListHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2()
  
  def get(self):
    key = Connection(info=self.request.headers.get('User-Agent'), status='setup').put()
    token = channel.create_channel(str(key.id()))
    self.response.write(self.jinja2.render_template('index.html', token=token))

class ConnectHandler(webapp2.RequestHandler):
  def post(self):
    client_id = self.request.get('from')
    logging.getLogger().info('{0} is connected'.format(client_id))
    con = Connection.get_by_id(int(client_id))
    con.status = 'connected'
    con.put()

class DisconnectHandler(webapp2.RequestHandler):
  def post(self):
    client_id = self.request.get('from')
    logging.getLogger().info('{0} is disconnected'.format(client_id))
    con = Connection.get_by_id(int(client_id))
    con.status = 'disconnected'
    con.put()

app = webapp2.WSGIApplication([
  ('/_ah/channel/connected/', ConnectHandler),
  ('/_ah/channel/disconnected/', DisconnectHandler),
  ('/', ListHandler)],
  debug=True)
