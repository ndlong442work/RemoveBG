echo "Starting app on PORT=$PORT"
gunicorn -w 4 -b 0.0.0.0:$PORT app:app