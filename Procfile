web: gunicorn flask_examen:app
init: source venv/bin/activate flask db init flask db migrate flask db upgrade FLASK_CONFIG=production FLASK_APP=run
