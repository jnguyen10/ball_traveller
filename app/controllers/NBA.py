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

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        url = "https://erikberg.com/nba/teams.json"
        headers = {'User-agent': "MyRobot:1.0 email@example.com"}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req).read()

        return self.load_view('index.html', response=response)

    def retrieve_teams(self):
        print "RETRIEVING TEAMS"

        url = "https://erikberg.com/nba/teams.json"
        headers = {'User-agent': "MyRobot:1.0 email@example.com"}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req).read()


        # notice this is 'requests' not 'request'
        # we are using the request modules, 'get' function to send a request from our controller
        # then we use ".content" to get the content we are looking for

        return self.load_view('index.html', response=response)
