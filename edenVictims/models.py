from django.db import models

# Create your models here.
class victims_data(models.Model):
    name = models.CharField(max_length=150)
    plot_no = models.CharField(max_length=25)
    project_name = models.CharField(max_length=150)
    paid_amount = models.FloatField()
    cnic = models.CharField(max_length=50)
    whatsapp_group = models.CharField(max_length=150, default="Eden Victims Group")
    receipt_no = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    country = models.CharField(max_length=50,  default="Pakistan")
    city = models.CharField(max_length=50, default="Lahore")
    additional_details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

     # renames the instances of the model 
        # with their title name 
    def __str__(self): 
        return self.name 

