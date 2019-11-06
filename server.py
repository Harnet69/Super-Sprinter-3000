from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


# index page
@app.route('/')
def route_index():
    stories_list = data_handler.get_data_from_file()  # list of user stories
    return render_template('index.html', stories_headers=data_handler.DATA_HEADER, user_stories=stories_list)


# add new user story
@app.route('/story', methods=['GET', 'POST'])
def route_story():
    if request.method == 'POST':  # if user submit new story by a form
        user_data_input = request.form  # got data from form
        stories_list = data_handler.get_data_from_file()  # list of user stories
        if stories_list:
            max_id = max(stories_list)  # get the last story id
            try:
                new_story_id = int(max_id[0]) + 1  # give to new user story the next id
            except ValueError:
                print("It's not a number")
        else:
            new_story_id = 0  #  if it's the first story
        user_store_data = []
        user_store_data.append(new_story_id)
        user_store_data.append(user_data_input["story_title"])
        user_store_data.append(user_data_input["user_story"])
        user_store_data.append(user_data_input["acc_crit"])
        user_store_data.append(user_data_input["business_value"])
        user_store_data.append(user_data_input["estimation"])
        user_store_data.append(user_data_input["status"])

        data_handler.write_data_to_file(user_store_data)  # write the story to a file
        return redirect('/')

    else:
        return render_template('story.html', statuses=data_handler.STATUSES)  # if a request method if GET


# edit user story
@app.route('/story/<int:post_id>', methods=['GET', 'POST'])
def route_edit_story(post_id):
    user_data_input = request.form  # get data from form to dictionary
    stories_list = data_handler.get_data_from_file()  # list of user stories
    story_to_edit = [x for x in stories_list if str(x[0]) == str(post_id)]  # find the story by id

    if request.method == "POST":
        updated_story = []  # updated story from form
        updated_story.append(user_data_input["story_id"])
        updated_story.append(user_data_input["story_title"])
        updated_story.append(user_data_input["user_story"])
        updated_story.append(user_data_input["acc_crit"])
        updated_story.append(user_data_input["business_value"])
        updated_story.append(user_data_input["estimation"])
        updated_story.append(user_data_input["status"])

        updated_stories = [] # updated by user stories
        for story in stories_list:
            if story[0] == updated_story[0]:  # if it's the updated story
                updated_stories.append(updated_story)
            else:
                updated_stories.append(story)

        data_handler.write_data_to_file(updated_stories, False)  # rewrite stories file by ONE TRANSACTION
        return redirect('/')

    if story_to_edit:  # check if typed by user in a browser line story id exists
        return render_template('story.html', statuses=data_handler.STATUSES, story_to_edit=story_to_edit[0])
    else:
        error_message = f"Store with id = {post_id} doesn't exist!"
        return render_template('error_page.html', error_message=error_message)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
