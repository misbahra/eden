from django.forms import ModelForm
from django import forms
from edenVictims.models import *

 
# define the class of a form
class edenVictimsForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        # write the name of models for which the form is made
        model = victims_data        
 
        # Custom fields
        #fields =["username", "gender", "text"]
        fields = "__all__"
 
    # this function will be used for the validation
    def clean(self):
        print('in clean')
        # data from the form is fetched using super function
        super(edenVictimsForm, self).clean()
         
        # extract the username and text field from the data
        # username = self.cleaned_data.get('username')
        # text = self.cleaned_data.get('text')
        name = self.cleaned_data.get('name')
        plot_no = self.cleaned_data.get('plot_no')
        project_name = self.cleaned_data.get('project_name')
        paid_amount = self.cleaned_data.get('paid_amount')
        cnic = self.cleaned_data.get('cnic')
        whatsapp_group = self.cleaned_data.get('whatsapp_group')
        receipt_no = self.cleaned_data.get('receipt_no')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        additional_details = self.cleaned_data.get('additional_details')
        country = self.cleaned_data.get('country')
        city = self.cleaned_data.get('city')
        print('in clean 2')

        

        #created_on = datetime.today()
 
        # # conditions to be met for the username length
        # if len(username) < 5:
        #     self._errors['username'] = self.error_class([
        #         'Minimum 5 characters required'])
        # if len(text) <10:
        #     self._errors['text'] = self.error_class([
        #         'Post Should Contain a minimum of 10 characters'])
        is_error = False
        if  name == None :
            is_error = True
            self._errors['name'] = self.error_class([
                'Name is required'])

        # if  email == None :
        #     is_error = True
        #     self._errors['email'] = self.error_class([
        #         'Email is required'])

        if  phone == None :
            is_error = True
            self._errors['phone'] = self.error_class([
                'Phone is required'])

        if  plot_no == None :
            is_error = True
            self._errors['plot_no'] = self.error_class([
                'Plot no. is required'])

        if  paid_amount == None :
            is_error = True
            self._errors['paid_amount'] = self.error_class([
                'Paid amount is required'])

        if  project_name == None :
            is_error = True
            self._errors['project_name'] = self.error_class([
                'Project name is required'])

        if  cnic == None :
            is_error = True
            self._errors['cnic'] = self.error_class([
                'cnic is required'])

        if  receipt_no == None :
            is_error = True
            self._errors['receipt_no'] = self.error_class([
                'Receipt no. is required'])

        if  email == None :
            self.cleaned_data['email'] = "none@none.com"

        if  whatsapp_group == None :
            self.cleaned_data['whatsapp_group'] = "Eden Mutasreen Ki Awaz 7"
            

        if  country == None :
            self.cleaned_data['country'] = "Pakistan"
            

        if  city == None :
            self.cleaned_data['city'] = "Lahore"
            

        if  additional_details == None :
            self.cleaned_data['additional_details'] = "Nil"
            

        if is_error == False:
            self._errors = []
           

        print(self.cleaned_data) 
        print('in clean 3')        
                #messages.warning(request,'Please fill all required fields')
        #if  name == '' or email == '' or phone == '' or plot_no == '' or paid_amount == '' or project_name == '' or cnic == '' or receipt_no == '' :
        #        self._errors['name'] = self.error_class([
        #        'Name is required'])

        # return any errors if found
        return self.cleaned_data