from flask import Flask , render_template , jsonify

app = Flask(__name__,template_folder="temps")

@app.route("/")
def root():
    return jsonify({"hola":"mujer"})


app.run(debug=True)
