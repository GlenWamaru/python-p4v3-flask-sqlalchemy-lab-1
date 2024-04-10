from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)  # Initialize SQLAlchemy

migrate = Migrate(app, db)  # Initialize Flask-Migrate

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake_by_id(id):
    # Query the database for the earthquake with the provided ID
    earthquake = Earthquake.query.filter_by(id=id).first()

    if earthquake:
        # Return JSON response with earthquake information
        return jsonify({
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }), 200
    else:
        # Return 404 error message if earthquake not found
        return jsonify({"message": f"Earthquake {id} not found."}), 404



if __name__ == '__main__':
    app.run(port=5555, debug=True)
