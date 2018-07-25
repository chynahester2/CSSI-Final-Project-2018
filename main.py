import webapp2
import jinja2
import os
from google.appengine.api import users
from models import User

the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True
)

def logged_in():
    user = users.get_current_user()
    status = ""
    if user:
        status = "Sign Out"
    else:
        status = "Sign In"
    return status

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        status = logged_in()
        link = users.create_logout_url('/login')
        if status == "Sign In":
            link = '/login'
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        temp_dict = {'status': status, 'link': link}
        self.response.write(welcome_template.render(temp_dict))

class DiscountPage(webapp2.RequestHandler):
    def get(self):
        discount_template = the_jinja_environment.get_template('templates/discount.html')
        self.response.write(discount_template.render())

class EventsPage(webapp2.RequestHandler):
    def get(self):
        events_template = the_jinja_environment.get_template('templates/events.html')
        self.response.write(events_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        # login_template = the_jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        if not user:
            self.response.write('''
                Please log in to our site! <br>
                <a href="%s">Sign in</a><br><br>
                Or sign up now!<br><a href="%s">Sign Up</a>'''
                % (users.create_login_url('/login'), users.create_login_url('/login')))
        else:
            email_address = user.nickname()
            cssi_user = User.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">Sign Out</a>' %(users.create_logout_url('/login'))
            if cssi_user:
                self.response.write('''Welcome %s %s (%s)! <br> You go to %s! <br> %s''' % (cssi_user.first_name, cssi_user.last_name, cssi_user.college, email_address, signout_link_html))
            else:
                self.response.write('''
                    Please Sign Up %s!<br>
                    <form method="post" action="/login">
                    <input type="text" name="first_name">
                    <input type="text" name="last_name">
                    <br>
                    <select name="college">
                    <option value="" disabled selected>Choose your college</option>
                    <option value="Georgia Tech">Georgia Tech</option>
                    <option value="Georgia State University">Georgia State University</option>
                    <option value="Emory University">Emory University</option>
                    <option value="Spelman College">Spelman College</option>
                    </select>
                    <br>
                    <input type="submit">
                    </form>
                    <br>%s''' % (email_address, signout_link_html))
    def post(self):
        user = users.get_current_user()
        self.response.write('You are now logged in!')
        self.response.write('''<a href="%s">Sign Out</a>'''% users.create_logout_url('/'))
        cssi_user = User(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            college=self.request.get('college'),
            id=user.user_id())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s %s! You go to %s' % (cssi_user.first_name, cssi_user.last_name, cssi_user.college))
class BooksPage(webapp2.RequestHandler):
    def get(self):
        books_template = the_jinja_environment.get_template('templates/books.html')
        self.response.write(books_template.render())

class SpecificEventPage(webapp2.RequestHandler):
    def get(self):
        event_template = the_jinja_environment.get_template('templates/event.html')



app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/discounts', DiscountPage),
    ('/events', EventsPage),
    ('/login', LoginPage),
    ('/books', BooksPage),
    ('/event', SpecificEventPage)
], debug=True)
