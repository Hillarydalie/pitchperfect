class Config:
    DEBUG=True
    SECRET_KEY='jklsjgkljskljgiorjiosnklfiowpnbriorbo'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://hillarydalie:password@localhost:5432/pitchperfect'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

 # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")