from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
def route_index():
    stories_list = data_handler.get_data_from_file()
    return render_template('index.html', stories_headers = data_handler.DATA_HEADER, user_stories = stories_list)


@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
