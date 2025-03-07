echo "Starting app on PORT=$PORT"
gunicorn -b 0.0.0.0:$PORT app:app