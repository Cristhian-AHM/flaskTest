from flask import Flask, request
from flask_restful import Resource, Api
import twitter

app = Flask(__name__)
api = Api(app)

CONSUMER_KEY = 'ItYG1kb3H16LDqyvF7WQg2Gyx'
CONSUMER_SECRET = 'b1Nyk2YRGBtBMAJZc49iA3bMdlPHOKQP0flGnn6Ih7yyYUkpzI'
OAUTH_TOKEN = '1062036810388389888-S8y8shsVj0BTh8IhZV5zdQJANbjjqh'
OAUTH_TOKEN_SECRET = 'pYK5jW5EZA02JKn2r9LqaMXlmrQ50sZT72gfsvYGH1gr4'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)


class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}
    
    def post(self):
        some_json = request.get_json()
        return {'You sent': some_json}, 201

class Multi(Resource):
    

    def get(self, num):
        return {'result': num*10, 'Twitter Api': world_trends}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == "__main__":
    app.run()