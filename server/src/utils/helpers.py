# src/utils/helpers.py

def serialize_task(task):
    return {
        'id': task.id,
        'title': task.title,
        'completed': task.completed,
        'children': [serialize_task(child) for child in task.children]
    }
