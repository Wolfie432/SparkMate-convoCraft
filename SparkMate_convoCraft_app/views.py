# myapp/views.py
from django.http import JsonResponse
from .chatterBot import chatterbot_instance

def get_bot_response(request):
    user_input = request.GET.get('user_input', '')
    response = chatterbot_instance.get_response(user_input).text
    print( response )
    return JsonResponse({'response': response})
