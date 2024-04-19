from flask import Flask, render_template, request
import qrcode
# used to store memory
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def generateQR():
    memory = BytesIO()
    data = request.form.get("link")
    img = qrcode.make(data)
    img.save(memory)
    # seek() fun reads the file from the absolute start rather than from the  middle or end
    memory.seek(0)
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img)


if __name__ == '__main__':
    # debug = True does hot reloading for us2
    app.run(debug=True)
