from config import app, db
from server.routes import dashboard, developer, organization 


if __name__ == "__main__":
    app.run(debug=True)