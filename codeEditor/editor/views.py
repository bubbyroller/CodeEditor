from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess

# Create your views here.
def editor_page(request):
    return render(request, 'editor.html')

@csrf_exempt  
def run_code(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code', '')
            language = request.POST.get('language', '')

            if language == 'python':
                result = run_python_code(code)
            else:
                result = "Language not supported for execution."

            return JsonResponse({'result': result})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})

# Functions for python code execution
def run_python_code(code):
    try:
        result = subprocess.check_output(['python', '-c', code], text=True, timeout=5)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

