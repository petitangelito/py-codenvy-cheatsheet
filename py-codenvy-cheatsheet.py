# Copyright 2014 Arn-O. See the LICENSE file at the top-level directory of this
# distribution and at
# https://github.com/Arn-O/py-codenvy-cheatsheet/blob/master/LICENSE

import timeit
import webapp2

from google.appengine.api import memcache

MEMCACHE_VAR_KEY = 'cached_variable'

def get_divisors(number):
    '''Compute the divisors and the duration time (ms).'''
    start_time = timeit.default_timer()
    divisors = []
    for i in range(1, int(number/2) ):
        if not number%i:
            divisors.append(i)
    end_time = timeit.default_timer() 
    duration = (end_time - start_time) * 1000
    return divisors, duration

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

class Stone2(webapp2.RequestHandler):
  
  def get(self):
    divisors, duration = get_divisors(10000)
    output_str = str(divisors) + '\n'
    output_str += 'Total computation time: ' + str(duration) + ' ms'
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
    ('/stone2', Stone2),
  ], debug=True)
