

from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


@app.route("/health")
def health():
	return jsonify({"status": "healthy"})

@app.route("/db-check")
def db_check():
	try:
		connection = psycopg2.connect(
			host=os.getenv("DB_HOST", "postgres"),
			database=os.getenv("DB_NAME", "ecommerce"),
			user=os.getenv("DB_USER", "admin"),
			password=os.getenv("DB_PASSWORD", "StrongPassword123"),
			port=os.getenv("DB_PORT", "5432")
		)

		connection.close()

		return jsonify({
			"database": "connected"
		})

	except Exception as e:
		return jsonify({
			"database": "failed",
			"error": str(e)
		}), 500

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
