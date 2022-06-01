from django.http import HttpResponseNotFound, HttpResponseServerError
import json


def error404(request, exception):
    response_data = {}
    response_data["success"] = False
    response_data["detail"] = "Not found."
    return HttpResponseNotFound(
        json.dumps(response_data), content_type="application/json"
    )


def error500(request, exception):
    response_data = {}
    response_data["success"] = False
    response_data["detail"] = "Server Error"
    return HttpResponseServerError(
        json.dumps(response_data), content_type="application/json"
    )
