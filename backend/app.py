from flask import Flask, jsonify
import psycopg2, os

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "postgres"),
            dbname=os.getenv("DB_NAME", "appdb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "password")
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from Postgres!'")
        msg = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"message": msg})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
