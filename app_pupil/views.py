# views.py
from django.http import HttpResponse

def index(request, id=None):
    
    pupils = [
        {'id': 1, 'name': 'murod', 'all': 33, 'grade': 'next'},
        {'id': 2, 'name': 'nurbek', 'all': 25, 'grade': 'next'},
        {'id': 3, 'name': 'azizbek', 'all': 26, 'grade': 'next'},
        {'id': 4, 'name': 'umar', 'all': 19, 'grade': 'next'},
        {'id': 5, 'name': 'obidjon', 'all': 20, 'grade': 'next'},
    ]
    
    if id is not None:
        for pupil in pupils:
            if pupil['id'] == id:
                return HttpResponse(
                    f"<p>ID: {pupil['id']}</p>"
                    f"<p>Name: {pupil['name']}</p>"
                    f"<p>All: {pupil['all']}</p>"
                    f"<p>Grade: {pupil['grade']}</p>"
                )
        return HttpResponse('Pupil not found', status=404)
    
    response = "<h1>Students Information</h1>"
    for pupil in pupils:
        response += (
            f"<p>ID: {pupil['id']}</p>"
            f"<p>Name: {pupil['name']}</p>"
            f"<p>All: {pupil['all']}</p>"
            f"<p>Grade: {pupil['grade']}</p><br>"
        )
    
    return HttpResponse(response)

