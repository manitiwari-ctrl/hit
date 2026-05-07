from flask import Flask, Response
import time
import os

app = Flask(__name__)

@app.route("/stream")
def stream():
    def generate():
        while True:
            yield "data: ping\n\n"
            time.sleep(1)

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
