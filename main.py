import os
import re
import jinja2
import webapp2

# To DEBUG the app.
import logging
logging.info('First logging INFO!')
logging.warning('First logging WARNING!')

template_dir = os.path.join(os.path.dirname(__file__), 'www')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               extensions=['jinja2.ext.autoescape'],
                               autoescape=True)  # autoescape is important for security!!

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        template = jinja_env.get_template(template)
        return template.render(params) # parameters can also be a dictionary!
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def render_front(self):
        self.render("index.html")

    def get(self):
        self.render_front() # draw main page

class About(Handler):
    def get(self):
        self.render("about.html")

class Projects(Handler):
    def get(self):
        self.render("projects.html")

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/about', About),
                               ('/projects', Projects)
                              ],
                              debug = False)  # CHange to False during production
# The debug=True parameter tells webapp2 to print stack traces to the browser output if a handler encounters an error or raises an uncaught exception. This option should be removed before deploying the final version of your application, otherwise you will inadvertently expose the internals of your application.
