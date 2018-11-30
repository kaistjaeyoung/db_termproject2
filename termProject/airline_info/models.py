from django.db import models

# Create your models here.
class AirPlane(models.Model) :
    Airline =  models.CharField(null = False, max_length=30)
    AirPlane_code = models.CharField(null = False, max_length=20, primary_key = True, unique = True)
    Num_of_seat = models.IntegerField()
    Made_by_Company = models.CharField(max_length = 100)
    Maintenance_Day = models.IntegerField()
    Captain_code = models.ForeignKey('Flight_captain', on_delete=models.CASCADE)

    def __str__(self):
        return self.AirPlane_code

class Flight_captain(models.Model) :
    First_name = models.CharField(max_length = 100)
    Second_name = models.CharField(max_length = 100)
    Birthday = models.DateField()
    home_address = models.CharField(max_length = 100)
    ssn = models.IntegerField()
    C_code = models.CharField(primary_key = True, null = False, unique = True,max_length = 100)

    def __str__(self):
        return self.C_code

class AirPort(models.Model) :
    Ap_Code = models.CharField(primary_key = True, null = False, unique = True,max_length = 100)
    Terminal = models.CharField(max_length = 100)
    Gate = models.CharField(max_length = 100)
    Status = models.CharField(max_length = 100)
    Airplain_code = models.ForeignKey('AirPlane', on_delete= models.CASCADE)
    FTID = models.ForeignKey('From_to', on_delete=models.CASCADE)
    TID = models.ForeignKey('Time_line',on_delete=models.CASCADE)

    def __str__(self):
        return self.Ap_Code

class From_to(models.Model) :
    F_T_id = models.IntegerField(primary_key = True, null = False, unique = True)
    Departure_loc = models.CharField(max_length = 100)
    Arrival_loc = models.CharField(max_length = 100)

    def __str__(self):
        return self.F_T_id

class Time_line(models.Model) :
    T_id = models.IntegerField( primary_key = True, null = False, unique = True)
    Departure_time = models.DateField()
    Arrival_time = models.DateField()

    def __str__(self):
        return self.T_id



