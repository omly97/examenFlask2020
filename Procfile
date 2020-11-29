web: gunicorn run:app
init: source venv/bin/activate flask db init flask db migrate flask db upgrade export FLASK_CONFIG=production export FLASK_APP=run
