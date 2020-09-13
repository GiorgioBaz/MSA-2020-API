from flask import render_template, request, redirect, url_for, jsonify
from app import app

# Task = models.Task

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/steam/', methods = ['GET'])
def getSteamGames():
    steamId = request.form.get('steamId')

    # getGames(steamId)
    return redirect(url_for('index'))

@app.route('/stats')
def add_stats():
    return render_template("stats.html")
# @app.route('/task/', methods=['POST'])
# def add_item():
#     # Get data from form fields taskName and taskDescription
#     taskName = request.form.get('taskName')
#     taskDescription = request.form.get('taskDescription')
    
#     # Put data into a new Task item
#     new_item = Task(name=taskName, description=taskDescription)
    
#     # Add and commit the changes to the database
#     db.session.add(new_item)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/task/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     task = Task.query.filter_by(id=id).first()
    
#     # Check if Task exists
#     if (task != None):
#         msg = {
#             'message': 'Delete successful'
#         }
#         db.session.delete(task)
#         db.session.commit()
#         return jsonify(msg), 200
	
#     # Task does not exist
#     msg = {
#         'message': 'Task not found'
#     }
#     return jsonify(msg), 204

# @app.route('/task/<int:id>', methods=['GET', 'POST'])
# def view_task(id):
#     if (request.method == "GET"):
#         task = Task.query.filter_by(id=id).first()
#         return render_template('view_task.html', taskName=task.name, taskDescription=task.description, taskId=task.id)
#     elif (request.method == "POST"):
#         taskId = request.form.get('taskId')
#         taskName = request.form.get('taskName')
#         taskDescription = request.form.get('taskDescription')

#         task = Task.query.filter_by(id=id).first()
#         if (task != None):
#             task.name = taskName
#             task.description = taskDescription
#             db.session.add(task)
#             db.session.commit()
#         return redirect(url_for('index'))