from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail


def index(request):
    return render(request, "workshop_app/index.html")


def about(request):
    return render(request, "workshop_app/about.html")


def contacts(request):
    return render(request, "workshop_app/contacts.html")


def price(request):
    return render(request, "workshop_app/price.html")


def works(request):
    return render(request, "workshop_app/works.html")


def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            last_name = request.POST["last_name"]
            phone_number = request.POST["phone_number"]
            email = request.POST["email"]
            message = request.POST["message"]
            contact = Contact(
                name=name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message,
            )
            contact.save()
            message = (
                f"Сообщение из формы от \n{name} \n{last_name} \nНомер телефона: {phone_number} \nпочта: {email}"
                f" \n{message}"
            )
            e_mail("Появился новый желающий", message)
            return HttpResponse("Контакт сохранён")
        return HttpResponse(f"Ошибка валидации, {form.errors}")
    else:
        form = ContactForm()
        message = "Заполните форму"
        return render(
            request, "workshop_app/add_contact.html", {"form": form, "message": message}
        )


def e_mail(subject, content):
    send_mail(subject, content, "denis-s2@yandex.ru", ["denis-s2@yandex.ru"])


def show_clients(request):
    contact = Contact.objects.all()
    result = "<br>".join([str(contact) for contact in contact])
    return HttpResponse(result)
