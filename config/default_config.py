import os

#this is what our application uses by default, tha is why debug is set to true to understands all errors
  
#DEBUG = True
#SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
#AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True # this is also necessary for error_handler below by allowing extensions to propagte our app
#this is only set for cookies
SECRET_KEY= os.environ.get("APP_SECRET_KEY")  # could do app.config['JWT_SECRET_KEY'] if we prefer, will crash if user set up our app without it in this format
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_BLACKLIST_ENABLED = True

JWT_BLACKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens


class Config():
    pass


class DevelopmentConfig(Config):
    #DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adesupraptolaia:alta123@localhost/ecommerce'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://nathaniel:church75@localhost/ecommerces'
    
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    #AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True # this is also necessary for error_handler below by allowing extensions to propagte our app
    #this is only set for cookies
    SECRET_KEY= os.environ.get("APP_SECRET_KEY")  # could do app.config['JWT_SECRET_KEY'] if we prefer, will crash if user set up our app without it in this format
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    JWT_BLACKLIST_ENABLED = True

    JWT_BLACKLIST_TOKEN_CHECKS = [
        "access",
        "refresh",
    ]  # allow blacklisting for access and refresh tokens


class TestingConfig(Config):
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://nathaniel:church75@localhost/ecommerces_test'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URIS")
    #AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True # this is also necessary for error_handler below by allowing extensions to propagte our app
    #this is only set for cookies
    SECRET_KEY= os.environ.get("APP_SECRET_KEY")  # could do app.config['JWT_SECRET_KEY'] if we prefer, will crash if user set up our app without it in this format
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    JWT_BLACKLIST_ENABLED = True

    JWT_BLACKLIST_TOKEN_CHECKS = [
        "access",
        "refresh",
    ]  # allow blacklisting for access and refresh tokens
