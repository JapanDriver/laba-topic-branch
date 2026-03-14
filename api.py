import Flask
app = Flask(__name__)
@app.route("/localhost", methods=["GET"])
def localhost(): pass