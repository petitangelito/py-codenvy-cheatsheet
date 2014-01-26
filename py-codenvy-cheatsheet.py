# Copyright 2014 Arn-O. See the LICENSE file at the top-level directory of this
# distribution and at
# https://github.com/Arn-O/py-codenvy-cheatsheet/blob/master/LICENSE

import webapp2

from google.appengine.api import memcache

MEMCACHE_VAR_KEY = 'cached_variable'

class MainPage(webapp2.RequestHandler):
  
  def get(self):
    output_str = 'Hello, world!'
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(output_str)

class Stone1(webapp2.RequestHandler):
  
  def get(self):
    output_str = 'Bonjour, monde!'
    output_str += '\n'
    output_str += 'This is basically like formating a flat file'
    output_str += '\n'
    output_str += 'And remember all kind of variable can be displayed like a string'
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(output_str)    

#class Stone3(webapp2.RequestHandler):

#  def get(self):  
#    some_variable = memcache.get(MEMCACHE_VAR_KEY)
#    if some_variable is None:
#      output_str = 'Not initialized yet'
#      memcache.set(MEMCACHE_VAR_KEY, 0)
#    else:
#      output_str = 'Variable value: %s' % str(some_variable)
#      some_variable += 1
#      memcache.set(MEMCACHE_VAR_KEY, some_variable)
#    self.response.headers['Content-Type'] = 'text/plain'
#    self.response.write(output_str)  
    
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/stone1', Stone1),
#    ('/stone3', Stone3),
  ], debug=True)
