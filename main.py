import webapp2
import jinja2
import os
from google.appengine.api import users
from models import User
from models import Advice

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
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        discount_template = the_jinja_environment.get_template('templates/discount.html')
        self.response.write(discount_template.render(temp_dict))

class EventsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        events_template = the_jinja_environment.get_template('templates/events.html')
        temp_dict = {'status': status, 'link': link, 'college': college}
        self.response.write(events_template.render(temp_dict))
        if user:
            self.response.write('''This is your college %s'''%(college))
            self.response.write('''
                <h3>%s</h3>
                <p>This is the events page for %s</p>'''
                % (college, college))
            if college == "Georgia Tech":
                self.response.write('''
                <table>
                <tr>
                <td>
                <h4>Robot Improv Circus</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Friday, July 27, 2018</li>
                <li>Time &ndash; 10:00AM - 4:00PM</li>
                <li>Location &ndash; Tech Rec in the Student Center</li>
                <li>Description &ndash; The Expressive Machinery Lab (formerly the ADAM Lab), directed by Brian Magerko, presents a preview of the Robot Improv Circus &ndash; a virtual reality installation where participants will collaborate with a robotic virtual stage partner to play the Props Game</li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>End of Summer 2018 Term</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Friday, August 3, 2018</li>
                <li>Time &ndash; All Day</li>
                <li>Location &ndash; Georgia Tech Campus</li>
                <li>Description &ndash; End of Term - All Summer Sessions 2018</li>
                </ul>
                </td>
                </tr>
                </table>''')
            elif college == "Georgia State University":
                self.response.write('''
                <table>
                <tr>
                <td>
                <h4>Panther Band Camp</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Monday, August 13 - Saturday, August 18, 2018</li>
                <li>Time &ndash; All Day</li>
                <li>Location &ndash; Helen M. Aderhold Learning</li>
                <li>Description &ndash; The 2018-2019 Panther Band Auditions take place at the Atlanta campus. </li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>Feed Your Senses featuring Pianist Kenneth Banks, Jr.</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Wednesday, August 15, 2018</li>
                <li>Time &ndash; 12:00PM - 1:00PM</li>
                <li>Location &ndash; Rialto Center for the Arts</li>
                <li>Description &ndash; The program features a different artist or speaker each month providing a casual and fun insider&#39;s look at their craft.</li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>4th Annual Plays in a Day Theater Festival Showcase</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Saturday, August 25, 2018</li>
                <li>Time &ndash; 8:00PM - 10:00PM</li>
                <li>Location &ndash; Marvin Cole Auditorium</li>
                <li>Description &ndash; Students perform a set of plays that, 24 hours before, didn&#39;t exist. Within a single day, Students write, direct, rehearse, tech and perform completely new and original works of theatre.</li>
                </ul>
                </td>
                </tr>
                </table>''')
            elif college == "Emory University":
                self.response.write('''
                <table>
                <tr>
                <td>
                <h4>Emory Farmers Market</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Tuesday, July 31, 2018</li>
                <li>Time &ndash; 11:00AM - 3:00PM</li>
                <li>Location &ndash; Cox Hall Bridge</li>
                <li>Description &ndash; The Emory Farmers Market features fresh, seasonal local produce; artisanal bread; honey; other artisan products and baked goods; fair trade and organic coffee options; and diverse lunch options.</li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>SURE Research Symposium</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Thursday, August 2, 2018</li>
                <li>Time &ndash; 10:00AM - 2:30PM</li>
                <li>Location &ndash; Math/Science Center Lobby and Room N304</li>
                <li>Description &ndash; The SURE Research Symposium provides the opportunity for the SURE undergraduate researchers who have completed full-time research for 10-weeks this summer to present their research for all to see.</li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>End of Summer 2018 Term</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Friday, August 10, 2018</li>
                <li>Time &ndash; All Day</li>
                <li>Location &ndash; Emory University Campus</li>
                <li>Description &ndash; End of Term - All Summer Sessions 2018</li>
                </ul>
                </td>
                </tr>
                </table>''')
            else:
                self.response.write('''
                <table>
                <tr>
                <td>
                <h4>New Student Orientation</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Wednesday, August 8 - Tuesday, August 14, 2018</li>
                <li>Time &ndash; All Day</li>
                <li>Location &ndash; Spelman College Campus</li>
                <li>Description &ndash; Incoming freshman are formally introduced to Spelman College and tour the campus.</li>
                </ul>
                </td>
                </tr>
                <tr>
                <td>
                <h4>First Day of Classes</h4>
                <ul style="list-style-type: none">
                <li>Date &ndash; Wednesday, August 15, 2018</li>
                <li>Time &ndash; All Day</li>
                <li>Location &ndash; Spelman College Campus</li>
                <li>Description &ndash; The start of the Fall Term.</li>
                </ul>
                </td>
                </tr>
                </table>''')
        else:
            self.response.write('''
                <div class="tab">
                    <button class="tablinks" onclick="openCollege(event, 'Georgia Tech')">Georgia Tech</button>
                    <button class="tablinks" onclick="openCollege(event, 'Georgia State University')">Georgia State University</button>
                    <button class="tablinks" onclick="openCollege(event, 'Emory University')">Emory University</button>
                    <button class="tablinks" onclick="openCollege(event, 'Spelman College')">Spelman College</button>
                </div>

                <div id="Georgia Tech" class="tabcontent" style="display: none;">
                    <h3>Georgia Tech</h3>
                    <table>
                    <tr>
                    <td>
                    <h4>Robot Improv Circus</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Friday, July 27, 2018</li>
                    <li>Time &ndash; 10:00AM - 4:00PM</li>
                    <li>Location &ndash; Tech Rec in the Student Center</li>
                    <li>Description &ndash; The Expressive Machinery Lab (formerly the ADAM Lab), directed by Brian Magerko, presents a preview of the Robot Improv Circus &ndash; a virtual reality installation where participants will collaborate with a robotic virtual stage partner to play the Props Game</li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>End of Summer 2018 Term</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Friday, August 3, 2018</li>
                    <li>Time &ndash; All Day</li>
                    <li>Location &ndash; Georgia Tech Campus</li>
                    <li>Description &ndash; End of Term - All Summer Sessions 2018</li>
                    </ul>
                    </td>
                    </tr>
                    </table>
                </div>

                <div id="Georgia State University" class="tabcontent" style="display: none;">
                    <h3>Georgia State University</h3>
                    <table>
                    <tr>
                    <td>
                    <h4>Panther Band Camp</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Monday, August 13 - Saturday, August 18, 2018</li>
                    <li>Time &ndash; All Day</li>
                    <li>Location &ndash; Helen M. Aderhold Learning</li>
                    <li>Description &ndash; The 2018-2019 Panther Band Auditions take place at the Atlanta campus. </li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>Feed Your Senses featuring Pianist Kenneth Banks, Jr.</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Wednesday, August 15, 2018</li>
                    <li>Time &ndash; 12:00PM - 1:00PM</li>
                    <li>Location &ndash; Rialto Center for the Arts</li>
                    <li>Description &ndash; The program features a different artist or speaker each month providing a casual and fun insider&#39;s look at their craft.</li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>4th Annual Plays in a Day Theater Festival Showcase</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Saturday, August 25, 2018</li>
                    <li>Time &ndash; 8:00PM - 10:00PM</li>
                    <li>Location &ndash; Marvin Cole Auditorium</li>
                    <li>Description &ndash; Students perform a set of plays that, 24 hours before, didn&#39;t exist. Within a single day, Students write, direct, rehearse, tech and perform completely new and original works of theatre.</li>
                    </ul>
                    </td>
                    </tr>
                    </table>
                </div>

                <div id="Emory University" class="tabcontent" style="display: none;">
                    <h3>Emory University</h3>
                    <table>
                    <tr>
                    <td>
                    <h4>Emory Farmers Market</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Tuesday, July 31, 2018</li>
                    <li>Time &ndash; 11:00AM - 3:00PM</li>
                    <li>Location &ndash; Cox Hall Bridge</li>
                    <li>Description &ndash; The Emory Farmers Market features fresh, seasonal local produce; artisanal bread; honey; other artisan products and baked goods; fair trade and organic coffee options; and diverse lunch options.</li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>SURE Research Symposium</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Thursday, August 2, 2018</li>
                    <li>Time &ndash; 10:00AM - 2:30PM</li>
                    <li>Location &ndash; Math/Science Center Lobby and Room N304</li>
                    <li>Description &ndash; The SURE Research Symposium provides the opportunity for the SURE undergraduate researchers who have completed full-time research for 10-weeks this summer to present their research for all to see.</li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>End of Summer 2018 Term</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Friday, August 10, 2018</li>
                    <li>Time &ndash; All Day</li>
                    <li>Location &ndash; Emory University Campus</li>
                    <li>Description &ndash; End of Term - All Summer Sessions 2018</li>
                    </ul>
                    </td>
                    </tr>
                    </table>
                </div>

                <div id="Spelman College" class="tabcontent" style="display: none;">
                    <h3>Spelman College</h3>
                    <table>
                    <tr>
                    <td>
                    <h4>New Student Orientation</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Wednesday, August 8 - Tuesday, August 14, 2018</li>
                    <li>Time &ndash; All Day</li>
                    <li>Location &ndash; Spelman College Campus</li>
                    <li>Description &ndash; Incoming freshman are formally introduced to Spelman College and tour the campus.</li>
                    </ul>
                    </td>
                    </tr>
                    <tr>
                    <td>
                    <h4>First Day of Classes</h4>
                    <ul style="list-style-type: none">
                    <li>Date &ndash; Wednesday, August 15, 2018</li>
                    <li>Time &ndash; All Day</li>
                    <li>Location &ndash; Spelman College Campus</li>
                    <li>Description &ndash; The start of the Fall Term.</li>
                    </ul>
                    </td>
                    </tr>
                    </table>
                </div>''')

class LoginPage(webapp2.RequestHandler):
    def get(self):
        # login_template = the_jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        if not user:
            self.response.write('''
                Please log in to our site! <br>
                <a href="%s">Sign in</a><br><br>
                Or sign up now!<br><a href="%s">Sign Up</a><br><br>
                <a href="/">Go Home</a>'''
                % (users.create_login_url('/login'), users.create_login_url('/login')))
        else:
            email_address = user.nickname()
            cssi_user = User.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">Sign Out</a>' %(users.create_logout_url('/login'))
            if cssi_user:
                self.response.write('''Welcome %s %s (%s)! <br> You go to %s! <br> %s<br><br> <a href="/">Go Home</a>''' % (cssi_user.first_name, cssi_user.last_name, email_address, cssi_user.college, signout_link_html))
            else:
                self.response.write('''
                    Please Sign Up %s!<br>
                    <form method="post" action="/login">
                    <input type="text" name="first_name" placeholder="First Name">
                    <input type="text" name="last_name" placeholder="Last Name">
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
                    <br>%s
                    <br><br>
                    <a href="/">Go Home</a>''' % (email_address, signout_link_html))
    def post(self):
        user = users.get_current_user()
        self.response.write('You are now logged in!<br>')
        self.response.write('''<a href="%s">Sign Out</a><br><br>'''% users.create_logout_url('/'))
        cssi_user = User(
            first_name=self.request.get('first_name'),
            last_name=self.request.get('last_name'),
            college=self.request.get('college'),
            id=user.user_id())
        cssi_user.put()
        self.response.write('Thanks for signing up, %s %s!<br><a href="/">Go Home</a>' % (cssi_user.first_name, cssi_user.last_name))
class BooksPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        books_template = the_jinja_environment.get_template('templates/books.html')
        self.response.write(books_template.render(temp_dict))

class StressedPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        stressed_template = the_jinja_environment.get_template('templates/stressed.html')
        self.response.write(stressed_template.render(temp_dict))

class MuseumsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        museums_template = the_jinja_environment.get_template('templates/museums.html')
        self.response.write(museums_template.render(temp_dict))

class TechnologyPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        technology_template = the_jinja_environment.get_template('templates/technology.html')
        self.response.write(technology_template.render(temp_dict))

class ShoppingPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        shopping_template = the_jinja_environment.get_template('templates/shopping.html')
        self.response.write(shopping_template.render(temp_dict))

class DormPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        dorm_template = the_jinja_environment.get_template('templates/dorm.html')
        self.response.write(dorm_template.render(temp_dict))

class ClothesPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        clothes_template = the_jinja_environment.get_template('templates/clothes.html')
        self.response.write(clothes_template.render(temp_dict))

class LaptopPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        laptop_template = the_jinja_environment.get_template('templates/laptop.html')
        self.response.write(laptop_template.render(temp_dict))

class MusicPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        music_template = the_jinja_environment.get_template('templates/music.html')
        self.response.write(music_template.render(temp_dict))

class MeditationPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        meditation_template = the_jinja_environment.get_template('templates/meditation.html')
        self.response.write(meditation_template.render(temp_dict))

class SportPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        sport_template = the_jinja_environment.get_template('templates/sport.html')
        self.response.write(sport_template.render(temp_dict))

class ComedyPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        comedy_template = the_jinja_environment.get_template('templates/comedy.html')
        self.response.write(comedy_template.render(temp_dict))

class FoodPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        food_template = the_jinja_environment.get_template('templates/food.html')
        self.response.write(food_template.render(temp_dict))

class FestivalPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        festival_template = the_jinja_environment.get_template('templates/festival.html')
        self.response.write(festival_template.render(temp_dict))

class ConcertPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        concert_template = the_jinja_environment.get_template('templates/concert.html')
        self.response.write(concert_template.render(temp_dict))

class TheaterPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        theater_template = the_jinja_environment.get_template('templates/theater.html')
        self.response.write(theater_template.render(temp_dict))

class AttractionsPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        attractions_template= the_jinja_environment.get_template('templates/attractions.html')
        self.response.write(attractions_template.render(temp_dict))

class NonfictionPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        nonfiction_template = the_jinja_environment.get_template('templates/nonfiction.html')
        self.response.write(nonfiction_template.render(temp_dict))

class FictionPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        fiction_template = the_jinja_environment.get_template('templates/fiction.html')
        self.response.write(fiction_template.render(temp_dict))

class AdvicePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        advice_template = the_jinja_environment.get_template('templates/advice.html')
        self.response.write(advice_template.render(temp_dict))

class InputPage(webapp2.RequestHandler):
    def get(self):
        suggestions = Advice.query().fetch()
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college, 'suggestion': suggestions}
        input_template = the_jinja_environment.get_template('templates/input.html')
        if user:
            self.response.write(input_template.render(temp_dict))
            self.response.write('''
            <div id = "suggestions">
              <form method="post">
                <h4>Have any book suggestions? Enter them here:</h4>
                <p>Enter the book name and author name.</p>
                <br>
                <input type="text" name="book_name" placeholder="Enter book name">
                <br>
                <input type="text" name="author_name" placeholder="Enter author name">
                <br>
                <input type="submit">
              </form>
            <h4>View all suggestions
            <a href="/other"> here!</a></h4>
            </div>''')
        else:
            self.response.write(input_template.render(temp_dict))
            self.response.write('''You are not logged in. Please log in to add a book suggestion. <br><a href='/login'>Sign in</a>''')
    def post(self):
        book = self.request.get('book_name')
        author = self.request.get('author_name')
        user = users.get_current_user()
        cssi_user = User.get_by_id(user.user_id())
        first = cssi_user.first_name
        last = cssi_user.last_name
        college = cssi_user.college
        suggestion = Advice(book_name=book, author_name=author, user_first=first, user_last=last, user_college=college)
        suggestion.put()
        self.redirect('/input')

class OtherPage(webapp2.RequestHandler):
    def get(self):
        suggestions = Advice.query().fetch()
        user = users.get_current_user()
        cssi_user = User.get_by_id(user.user_id())
        first = cssi_user.first_name
        last = cssi_user.last_name
        college = cssi_user.college
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college, 'suggestion': suggestions}
        input_template = the_jinja_environment.get_template('templates/other.html')
        self.response.write(input_template.render(temp_dict))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        status = logged_in()
        link = users.create_logout_url('/login')
        college = ""
        if status == "Sign In":
            link = '/login'
        else:
            college = User.get_by_id(user.user_id()).college
        temp_dict = {'status': status, 'link': link, 'college': college}
        about_template = the_jinja_environment.get_template('templates/about.html')
        self.response.write(about_template.render(temp_dict))

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/discounts', DiscountPage),
    ('/events', EventsPage),
    ('/login', LoginPage),
    ('/books', BooksPage),
    ('/stressed', StressedPage),
    ('/museums', MuseumsPage),
    ('/technology',TechnologyPage),
    ('/shopping', ShoppingPage),
    ('/dorm', DormPage),
    ('/clothes', ClothesPage),
    ('/laptop',LaptopPage),
    ('/music', MusicPage),
    ('/meditation', MeditationPage),
    ('/events/sport', SportPage),
    ('/events/comedy', ComedyPage),
    ('/events/food', FoodPage),
    ('/events/festival', FestivalPage),
    ('/events/music', ConcertPage),
    ('/events/theater', TheaterPage),
    ('/events/attractions', AttractionsPage),
    ('/nonfiction', NonfictionPage),
    ('/fiction', FictionPage),
    ('/advice', AdvicePage),
    ('/input', InputPage),
    ('/about', AboutPage),
    ('/other', OtherPage)
], debug=True)
