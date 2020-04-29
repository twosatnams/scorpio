from flask import Flask, request, jsonify
from lib.globals import config, logger, ApplicationException
from lib.models import db, Stock
from lib.controllers import get_top_gainers
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)
app.app_context().push()
CORS(app)


@app.route('/serve/top_gainers', methods=['GET'])
def top_gainers():
    try:
        record_date = request.args.get('record_date')
        result = get_top_gainers(record_date)
        return jsonify(result)

    except ApplicationException as ex:
        logger.error(ex, exc_info=1)
        return jsonify({'error_code': 1, 'message': str(ex)}), 400

    except Exception as e:
        logger.error(e, exc_info=1)
        return jsonify({'error_code': 2, 'message': 'Failed during matching/lookup (unhandled exception)'}), 500


@app.route('/serve/accuracy', methods=['GET'])
def accuracy():
    try:
        
        print('nothing')

    except SearchException as ex:
        logger.error(ex, exc_info=1)
        return jsonify({'error_code': 1, 'message': str(ex)}), 400

    except Exception as e:
        logger.error(e, exc_info=1)
        return jsonify({'error_code': 2, 'message': 'Failed during matching/lookup (unhandled exception)'}), 500


@app.route('/serve/watchlist', methods=['GET'])
def watchlist():
    try:
        
        print('nothing')

    except SearchException as ex:
        logger.error(ex, exc_info=1)
        return jsonify({'error_code': 1, 'message': str(ex)}), 400

    except Exception as e:
        logger.error(e, exc_info=1)
        return jsonify({'error_code': 2, 'message': 'Failed during matching/lookup (unhandled exception)'}), 500


@app.route('/serve/signup', methods=['POST'])
def signup():
    try:
        print('nothing')
    except Exception as e:
        logger.error(e, exc_info=1)
        return jsonify({
            'error_code': 2,
            'message': 'Failed during set bounding box (unhandled exception)'
        }), 500


@app.route('/serve/healthcheck', methods=['GET'])
def healthcheck():
    # account = db.query(Account).filter(Account.id == 890).one()
    print('nothing')
    return 'Still alive'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)