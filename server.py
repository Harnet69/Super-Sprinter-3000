from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
def route_index():
    stories_list = data_handler.get_data_from_file()

    return render_template('index.html', stories_headers=data_handler.DATA_HEADER, user_stories=stories_list)


@app.route('/story', methods=['GET', 'POST'])
def route_story():
    if request.method == 'POST':
        user_data_input = request.form  # get data from form to dictionary

        user_store_data = []
        user_store_data.append("Id")  # TODO add appropriate function
        user_store_data.append(user_data_input["story_title"])
        user_store_data.append(user_data_input["user_story"])
        user_store_data.append(user_data_input["acc_crit"])
        user_store_data.append(user_data_input["business_value"])
        user_store_data.append(user_data_input["estimation"])
        user_store_data.append(user_data_input["status"])

        data_handler.write_data_to_file(user_store_data)
        return redirect('/')

    else:
        return render_template('story.html', statuses=data_handler.STATUSES)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
