from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def text_to_speech(request):

    if request.method=='POST':

        data = json.loads(request.body)
        input_text = data.get('input_text', None)
        if input_text is None:
            return JsonResponse({'error': 'Please include the input_text in the body.'}, status=401)

        print(input_text);

        
        # tacatron


        response_data = {
            'message': f'{input_text}',
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


