from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 again cheack"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's assigned port
    app.run(host="0.0.0.0", port=port)
