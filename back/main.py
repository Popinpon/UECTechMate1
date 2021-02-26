from flask import Flask, render_template, request, jsonify
import os


app = Flask(__name__, static_folder='../dist/static',
            template_folder='../dist')


@app.route('/get_test_data', methods=["POST"])
def get_test_data():
    return jsonify({"test_index_data": "いい感じのデータ: " + request.form["test_post_data"]})


@app.route('/youtube_data', methods=["POST"])
def get_youtube_data():
    return jsonify({"youtube_data": "youtube のいい感じのデータ: " + request.form["test_post_data"]})


@app.route('/twitter_data', methods=["POST"])
def get_twitter_data():
    return jsonify({"twitter_data": "twitter のいい感じのデータ: " + request.form["test_post_data"]})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
