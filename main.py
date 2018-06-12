import webapp2
import tools

class Main(webapp2.RequestHandler):

    def render_template(self, view_filename, template_dir=None, params=None):
        if params is None:
            params = {}
        view_dir = template_dir or 'views'
        jinja_env = tools.Config.config.get('template')
        template_env = jinja_env(tools.Config, view_dir).get_template(view_filename)
        self.response.write(template_env.render(params))

    def home(self):
        self.render_template('index.html')


routes = [
    webapp2.Route(r'/', handler=Main, name='home', handler_method='home', methods=['GET'])
]

app = webapp2.WSGIApplication(routes=routes, config=tools.Config.config, debug=True)
