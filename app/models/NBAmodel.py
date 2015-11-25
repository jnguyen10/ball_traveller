""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class NBAmodel(Model):
    def __init__(self):
        super(NBAmodel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    def get_all_users(self):
        print self.db.query_db("SELECT * FROM users")

    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    """
    If you have enabled the ORM you have access to typical ORM style methods.
    See the SQLAlchemy Documentation for more information on what types of commands you can run.
    """


    def find_team_link(self,id):
        query = "SELECT name, link FROM listings WHERE id = %s"
        data = [id]

        return self.db.query_db(query,data)


    def create(self, user_info):
        errors = []
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        if not user_info['username']:
            errors.append('Username cannot be blank')
        elif len(user_info['username']) < 2:
            errors.append('username must be at least 2 charaters long')

        if not user_info['email']:
            errors.append('Email cannot be blank')
        elif len(user_info['email']) < 2:
            errors.append('Email must be at least 2 charaters long')
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append('Email is not valid')

        if not user_info['password']:
            errors.append('Password cannot be blank')
        elif not user_info['password_confirm']:
            errors.append('Password confirmation cannot be blank')
        elif len(user_info['password']) < 5:
            errors.append('Password must be at least 5 charaters long')
        elif user_info['password'] != user_info['password_confirm']:
            errors.append('Passwords do not match')

        if errors:
            return {'status': False, 'errors': errors}

        pw_hash = self.bcrypt.generate_password_hash(user_info['password'])


        insert_query = "INSERT INTO users (username, email, password, created_at) VALUES (%s, %s, %s, now())"
        insert_data = [user_info['username'], user_info['email'], pw_hash]
        self.db.query_db(insert_query, insert_data)

        get_user_query = "SELECT id FROM users WHERE username = %s"
        insert_data = [user_info['username']]
        user_id = self.db.query_db(get_user_query, insert_data)
        print user_id

        insert_query = "INSERT INTO locations (user_id, street, city, state) VALUES (%s, %s, %s, %s)"
        insert_data = [user_id[0]['id'], user_info['street'], user_info['city'], user_info['state']]
        self.db.query_db(insert_query, insert_data)

        get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
        user = self.db.query_db(get_user_query)

        return {'status': True, 'user': user[0]}

    def sign_in(self, user_info):
        password = user_info['password']
        sign_in_query = 'SELECT * FROM users WHERE email = %s LIMIT 1'
        user_email = [user_info['email']]
        user = self.db.query_db(sign_in_query, user_email)
        if user and self.bcrypt.check_password_hash(user[0]['password'], user_info['password']):
            return {'status': True, 'user': user[0]}
        else:
            return {'status': False}

