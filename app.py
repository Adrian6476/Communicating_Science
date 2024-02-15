from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/svm')
def svm():
    return render_template('templates/SVM_interactive_charts.html')

@app.route('/kmeans')
def kmeans():
    return render_template('templates/k-means_interactive_charts.html')

if __name__ == '__main__':
    app.run(debug=True)
