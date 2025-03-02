from django.shortcuts import render
from django.http import JsonResponse
from .forms import InquiryForm

def inquiry_view(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Success"}, status=200)
        else:
            return JsonResponse({"message": "Error", "errors": form.errors}, status=400)

    form = InquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})

def inquiry_success(request):
    return render(request, 'inquiry_success.html')
