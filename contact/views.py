# contact/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']

            message_complet = f"Message de {nom} ({email})\n\n{sujet}\n\n{message}"

            send_mail(
                sujet,
                message_complet,
                'noreply@lebonberger.td',
                ['ecoledesantelebonberger@gmail.com'],
                fail_silently=False,
            )

            # Revenir à la même page avec un message
            return render(request, 'contact.html', {
                'form': ContactForm(),
                'envoye': True
            })

    return render(request, 'contact.html', {'form': form})
