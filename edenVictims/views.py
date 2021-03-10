from django.shortcuts import render,HttpResponse
from eden import settings
from datetime import datetime
from edenVictims.models import victims_data
from django.contrib import messages
from django.db.models import Q
from .forms import edenVictimsForm
import xlwt
       

# Create your views here.
def home(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'home.html')


def upload_data(request):

    if request.method == "POST":
        print("posting data")
        
        name = request.POST.get("name")
        plot_no = request.POST.get("plot_no")
        project_name = request.POST.get("project_name")
        paid_amount = request.POST.get("paid_amount")
        cnic = request.POST.get("cnic")
        whatsapp_group = request.POST.get("whatsapp_group")
        receipt_no = request.POST.get("receipt_no")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        city = request.POST.get("city")
        additional_details = request.POST.get("additional_details")
        
        if whatsapp_group == None:
            whatsapp_group = "Eden Victims"

        if country == None:
            country = "Pakistan"

        if city == None:
            city = "Lahore"

        if additional_details == None:
            additional_details = "Nil"

        # v_data =  victims_data(
        #                         "name" : name,
        #                         plot_no : plot_no,
        #                         project_name : project_name,
        #                         paid_amount : paid_amount,
        #                         cnic : cnic,
        #                         whatsapp_group : whatsapp_group,
        #                         receipt_no : receipt_no,
        #                         email : email,
        #                         phone : phone,
        #                         country : country,
        #                         city : city,
        #                         additional_details : additional_details
        #                     )

        print('posting')
        # Pass the form data to the form class
        # print(request.POST)

        details = edenVictimsForm(request.POST)
        # print(details)
        #details = v_data

        
       # In the 'form' class the clean function 
        # is defined, if all the data is correct 
        # as per the clean function, it returns true
        
        if details.is_valid(): 
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database   
            post = details.save(commit = False)
            print(post)
            # Finally write the changes into database
            post.save()  

            messages.success(request,'Successfully saved')
        
 
            # redirect it to some another page indicating data
            # was inserted successfully
            return render(request, 'view_data.html')
        else:
         
            # Redirect back to the same page if the data
            # was invalid
            form = details
            messages.warning(request,'Please fill all required fields')
            return render(request, "upload_data.html", {'form':form})  
   
    else:
 
        # If the request is a GET request then,
        # create an empty form object and 
        # render it into the page
        form = edenVictimsForm(None)   
        return render(request, 'upload_data.html', {'form':form})




    #    #validate data
    #     if  name == '' or email == '' or phone == '' or plot_no == '' or paid_amount == '' or project_name == '' or cnic == '' or receipt_no == '' :
    #             messages.warning(request,'Please fill all required fields')
        
    #     if messages:
    #        return render(request, 'upload_data.html')

    #     if not messages:
    #         vd = victims_data(
    #             name = name,
    #             plot_no = plot_no,
    #             project_name = project_name,
    #             paid_amount = paid_amount,
    #             cnic = cnic,
    #             whatsapp_group = whatsapp_group,
    #             receipt_no = receipt_no,
    #             email = email,
    #             additional_details = additional_details,
    #             created_on = created_on
    #         )
    #         vd.save()
    #         messages.success(request,'Data saved successfully')
    #         return render(request, 'view_data.html')
    # else:
    #     return render(request, 'upload_data.html')

# view your data
def view_data(request):

    if request.method == "POST":
        
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        allData = victims_data.objects.filter(Q(email=email) | Q(phone=phone))

        #allData = victims_data.objects.all()
        context= {'allData': allData , 'email' : email}
        return render(request, 'view_data.html', context)
    else:
        return render(request, 'view_data.html')

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-disposition'] = 'attachment; filename=edenvictims' + \
        str(datetime.now()) + '.xls' 
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('EdenVictims')
    row_num = 0

    font_style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    font_style.font=font

   
    
    columns = [ 'id',
                'name' ,
                'plot_no' ,
                'project_name' ,
                'paid_amount' ,
                'cnic' ,
                'whatsapp_group' ,
                'receipt_no' ,
                'email',
                'phone' ,
                'country' ,
                'city' ,
                'additional_details' ,
                'created_on' ]

    for col_num in range (len(columns)):
        ws.write(row_num , col_num , columns[col_num], font_style )

    font_style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = False
    font_style.font=font

    rows = victims_data.objects.all().values_list(
                'id',
                'name' ,
                'plot_no' ,
                'project_name' ,
                'paid_amount' ,
                'cnic' ,
                'whatsapp_group' ,
                'receipt_no' ,
                'email',
                'phone' ,
                'country' ,
                'city' ,
                'additional_details' ,
                'created_on' 
    )

    
    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num , col_num , str(row[col_num]), font_style )

    wb.save(response)
    return response
