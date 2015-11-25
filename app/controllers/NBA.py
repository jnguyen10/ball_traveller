"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import urllib
import urllib2


class NBA(Controller):
    def __init__(self, action):
        super(NBA, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """
        self.load_model('NBAmodel')
    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """

        return self.load_view('index.html')

    def create(self):
        user_info = request.form
        result = self.models['NBAmodel'].create(user_info)
        if result['status']:
            session['id'] = result['user']['id']
            session['username'] = result['user']['username']
            return self.load_view('logos.html')
        else:
            for msg in result['errors']:
                flash(msg)
            return redirect('/register')

    def sign_in(self):
        user_info = request.form
        result = self.models['NBAmodel'].sign_in(user_info)
        if result['status'] is True:
            # session['id'] = result['user']['id']
            # session['username'] = result['user']['username']
            return self.load_view('logos.html')
        else:
            flash('Invalid email or password')
            return redirect('/')

    def register(self):
        return self.load_view('register.html')

