import webapp2
import jinja2
import os

the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True
)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        

app = webapp2.WSGIApplication([
    ('/', WelcomePage)
], debug=True)
