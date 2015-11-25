"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from lxml import html
import requests
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

    def logos(self):

        return self.load_view('logos.html')

    def retrieve_teams(self):
        pass
        # print "Retrieve Teams"



        # url = "https://erikberg.com/nba/teams.json"
        # headers = {'User-agent': "MyRobot:1.0 email@example.com"}
        # req = urllib2.Request(url, headers=headers)
        # response = urllib2.urlopen(req).read()

        # return response

    def retrieve_listings(self, id):
        print "Retrieve Listings"
        team_data = self.models['NBAmodel'].find_team_link(id)

        print "TEAM DATA:", team_data


        url = team_data[0]['link']
        team = team_data[0]['name']

        response = requests.get(url).content

        return response


