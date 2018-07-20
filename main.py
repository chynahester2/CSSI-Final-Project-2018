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
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

class DiscountPage(webapp2.RequestHandler):
    def get(self):
        discount_template = the_jinja_environment.get_template('templates/discount.html')
        self.response.write(discount_template.render())

class EventsPage(webapp2.RequestHandler):
    def get(self):
        events_template = the_jinja_environment.get_template('templates/events.html')
        self.response.write(events_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/discount', DiscountPage),
    ('/events', EventsPage)
], debug=True)
