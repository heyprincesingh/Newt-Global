from django.shortcuts import render  # type: ignore
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages  # type: ignore
from django.core.mail import EmailMessage  # type: ignore


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = (
                f"Thank you for your submission, {first_name}. "
                f"Here are your data:\n{first_name}\n{last_name}\n{date}\n"
                f"Thank you!"
            )
            message = EmailMessage(
                subject="New form submission", body=message_body, to=[email]
            )
            message.send()

            messages.success(
                request, f"{first_name}, your form was submitted successfully!"
            )
        else:
            print(form.errors)
    else:
        form = ApplicationForm()

    return render(request, "index.html", {"form": form})
