from flask_graduation import create_app, db, models
from flask_migrate import Migrate
from flask_cors import CORS

app = create_app('develop')
app.app_context().push()
Migrate(app, db)

CORS(app, resources={
    r'/*': {"origins": "*"}
})


@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
