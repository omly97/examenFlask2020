web: gunicorn run:app
init: source venv/bin/activate 
init: flask db init 
init: flask db migrate 
init: flask db upgrade 
init: FLASK_CONFIG=production 
init: FLASK_APP=run
