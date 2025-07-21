from django.utils.safestring import mark_safe # 为了能够渲染markdown
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import UsrSubmission # 从本项目的.py文件导入函数时，不要加后缀
from chatlogic import send_to_ds
import markdown

# Create your views here.
def process_with_submission(request):
    if request.method == 'POST':
        usrinput = request.POST.get("usrinput", "")
        mod = request.POST.get("mode", "") == "on"
        abstract = request.POST.get("abstract", "") == "on"
        keep = request.POST.get("keep", "") == "on"
        temp = 1.0  # 或其他处理逻辑

        submission = UsrSubmission.objects.create(
            mode="mod" if mod else "default",
            usrinput=usrinput,
            abstract=abstract,
            keepit=keep,
            temp=temp,
        )

        reply = send_to_ds([
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": usrinput},
        ], usr_submission=submission)

        return JsonResponse({"reply": reply})
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)