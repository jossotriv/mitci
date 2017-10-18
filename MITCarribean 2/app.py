from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/energy')
def energy():
    return render_template('energy.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/housing')
def housing():
    return render_template('housing.html')

@app.route('/agriculture')
def agriculture():
    return render_template('agriculture.html')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
