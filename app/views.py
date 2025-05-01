from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail, BadHeaderError
from .models import BlogPost, Service
from django.conf import settings

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsletterSubscriber

def home(request):
    posts = BlogPost.objects.order_by('-created_at')[:6]  # Show latest 6 blogs
    return render(request, 'app/index.html', {'posts': posts})

def company_incorporation(request):
    return render(request, 'app/company_incorporation.html')

def compliance(request):
    return render(request, 'app/compliance.html')

def statutory_certification(request):
    return render(request, 'app/statutory_certification.html')

def compliance_secretaries(request):
    return render(request, 'app/compliance_secretaries.html')


def bank_services(request):
    return render(request, 'app/bank_services.html')

def secreterial_audits(request):
    return render(request, 'app/secreterial_audits.html')

def rbi_fema_compliance(request):
    return render(request, 'app/rbi_fema_compliance.html')

def corporate_advisory(request):
    return render(request, 'app/corporate_advisory.html')

def other_services(request):
    return render(request, 'app/other_services.html')

def sexual_harasment(request):
    return render(request, 'app/sexual_harasment.html')

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'app/blog-details.html', {'post': post})

def investment_fundraising(request):
    return render(request, 'app/investment_fundraising.html')


@csrf_exempt
def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        try:
            validate_email(email)
            obj, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({"status": "success", "message": "Subscribed successfully!"})
            else:
                return JsonResponse({"status": "exists", "message": "Already subscribed."})
        except ValidationError:
            return JsonResponse({"status": "error", "message": "Invalid email."})
    return JsonResponse({"status": "error", "message": "Invalid request."})




def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'app/service_detail.html', {'service': service})

from .models import ServiceCategory

def service_categories(request):
    return {'service_categories': ServiceCategory.objects.prefetch_related('children', 'services')}

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Message from {name} <{email}>:\n\n{message}"
        print("Sendding................")
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],  # your email here
            )
            return render(request, "index.html", {"success": True})
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
    return render(request, "index.html")


