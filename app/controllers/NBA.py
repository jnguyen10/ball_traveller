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

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """


        return self.load_view('index.html')

    def retrieve_teams(self):
        print "Retrieve Teams"



        # url = "https://erikberg.com/nba/teams.json"
        # headers = {'User-agent': "MyRobot:1.0 email@example.com"}
        # req = urllib2.Request(url, headers=headers)
        # response = urllib2.urlopen(req).read()

        # return response

    def data_scraping(self):
        pass

    def retrieve_listings(self):
        print "Retrieve Listings"

        url = "https://www.ticketcity.com/catalog/events/performer/1354/11-24-2015/11-24-2033?PageNum=1&PageSize=25"

        response = requests.get(url).content

        # print response

        return response



