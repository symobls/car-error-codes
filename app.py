from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample error codes data
error_codes = {
    '100': {'message': 'خطأ عام'},
    '101': {'message': 'خطأ في الاتصال'},
    '102': {'message': 'خطأ في التهيئة'},
}

@app.route('/api/errors', methods=['GET'])
def get_errors():
    return jsonify(error_codes), 200

@app.route('/api/errors/<code>', methods=['GET'])
def get_error(code):
    error = error_codes.get(code)
    if error:
        return jsonify({code: error}), 200
    else:
        return jsonify({'error': 'الكود غير موجود'}), 404

@app.route('/api/search', methods=['POST'])
def search_errors():
    search_term = request.json.get('query')
    results = {code: msg for code, msg in error_codes.items() if search_term in msg['message']}
    return jsonify(results), 200

# Error handling in Arabic
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'لم يتم العثور على المورد'}), 404

if __name__ == '__main__':
    app.run(debug=True)