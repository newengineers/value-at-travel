from flask_session import Session

from portal.routing import app

if __name__ == '__main__':
    app_session = Session()
    app_session.init_app(app)
    app.run()
