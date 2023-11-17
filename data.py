from flask import Flask, render_template, jsonify
import livepopulartimes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 这里是正确的位置

@app.route('/get_popular_times')
def get_popular_times():
    formatted_address = "Morton Williams Supermarkets, 2941 Broadway, New York, NY, USA"
    data = livepopulartimes.get_populartimes_by_address(formatted_address)
    if 'current_popularity' in data:
        populartimes = data['current_popularity']
        out_data = populartimes
    else:
        out_data = "Unable to read the popularity of this place"
    return jsonify(out_data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
