# Copyright 2014 Arn-O. See the LICENSE file at the top-level directory of this
# distribution and at
# https://github.com/Arn-O/py-codenvy-cheatsheet/blob/master/LICENSE

import timeit
import webapp2

from google.appengine.api import memcache

MEMCACHE_I_KEY = 'cached_i'
MEMCACHE_DIVISORS_KEY = 'cached_divisors'

def get_divisors(number):
  '''Compute the divisors and the duration time (ms).'''
  start_time = timeit.default_timer()
  divisors = []
  for i in range(1, int(number/2) + 1):
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

class Stone3(webapp2.RequestHandler):
  
  def get(self):
    number = 1000
    i = memcache.get(MEMCACHE_I_KEY)
    divisors = memcache.get(MEMCACHE_DIVISORS_KEY)
    if i is None:
      i = 1
      divisors = []
    output_str = 'Number to divide: ' + str(number) + '\n'
    output_str += 'Iteration: ' + str(i) + ' - '
    if not number%i:
      output_str += 'New divisor found!' + '\n'
      divisors.append(i)
    else:
      output_str += 'This is not a divisor' + '\n'
    output_str += str(divisors) + '\n'
    if i <  (int(number/2) + 1):
      i += 1
    else:
      output_str += 'Last iteration' + '\n'
    memcache.set(MEMCACHE_I_KEY, i)
    memcache.set(MEMCACHE_DIVISORS_KEY, divisors)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(output_str)  
    
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/stone1', Stone1),
    ('/stone2', Stone2),
    ('/stone3', Stone3),
  ], debug=True)
