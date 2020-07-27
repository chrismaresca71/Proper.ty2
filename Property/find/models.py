# From Django
from django.db import models
from django.utils.translation import ugettext as _
from django_localflavor_us.models import USStateField
from django.utils import timezone
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# From Project
from registration.models import *




class Address(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    address = models.CharField(_("address"), max_length=128, default="")
    city = models.CharField(_("city"), max_length=64, default="")
    state = USStateField(_("state"), default="")
    zip_code = models.CharField(_("zip code"), max_length=5, default="")

    def __str__(self):
        return self.address
    
    class Meta:
        db_table = "Address"


class Home(models.Model):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,

    )

    yes_no = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    

    
    price = models.PositiveIntegerField(validators = [ MaxValueValidator(750000000)])
    square_footage = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='primary_house', blank=True, null=True)
    current_date = models.DateField(default=timezone.now)

    # Facts and Features

    home_types = (
        ('Single Family', 'Single Family'),
        ('Duplex', 'Duplex'),
        ('Multi-Family', 'Multi-Family'),
        ('Townhome', 'Townhome'),
        ('Manufactured Home', 'Manufactured Home')

    )

    heating_systems = (
        ('Forced Air (gas)', 'Forced Air (gas)'),
        ('Electric', 'Electric'),
        ('Geothermal', 'Geothermal'),
        ('Radiant Heat', 'Radiant Heat'),
        ('Steam Radiant Heat', 'Steam Radiant Heat'),
        (None, 'None')

    )

    cooling_systems = (
        ('Central', 'Central'),
        ('Ductless', 'Ductless'),
        ('Heat Pump', 'Heat Pump'),
        ('Evaoporative', 'Evaporative'),
        (None, 'None')
    )

    home_type = models.CharField(max_length = 30 ,null=True, choices=home_types, default= 'Single Family')
    year_built = models.PositiveIntegerField(default=2020, validators = [ MaxValueValidator(2020)])
    heating_system1 = models.CharField(max_length = 50, null=True, choices=heating_systems, default='Electric', verbose_name='Main Heating')
    heating_system2 = models.CharField(max_length = 50, null=True, choices=heating_systems, default='None', verbose_name= 'Other Heating' )
    cooling_system = models.CharField(max_length = 50, null=True, choices=cooling_systems, default='Central')
    parking_spaces = models.PositiveIntegerField(default=2, validators = [ MaxValueValidator(15)], null=True)

    # Interior Features
    master_bedroom = models.CharField(max_length = 10, default="Yes", verbose_name='Master Bedroom?', choices=yes_no)
    master_bathroom = models.CharField(max_length = 10, default="Yes", verbose_name='Master Bath?', choices=yes_no)
    full_bathrooms = models.PositiveIntegerField(null=True)
    three_quarter_bathrooms = models.PositiveIntegerField(null=True, verbose_name='3/4 Bathroom')
    half_bathrooms = models.PositiveIntegerField(null=True, verbose_name='1/2 Bathroom')
    one_quarter_bathrooms = models.PositiveIntegerField(null=True, verbose_name='1/4 Bathroom')
    appliances = models.TextField(null=True, blank=True, default="NA")
    other_interior_features = models.TextField(null=True, blank=True)

    #Exterior Features
    pool_choices = (
        (None, 'None'),
        ('In-ground', 'In-ground'),
        ('Above Ground', 'Above Ground')
    )


    attached_garage = models.CharField(max_length = 10, default="Yes", choices=yes_no)
    levels = models.PositiveIntegerField(validators = [ MaxValueValidator(10)],null=True)
    stories = models.PositiveIntegerField(validators = [ MaxValueValidator(10)],null=True)
    pool = models.CharField(max_length=30, choices=pool_choices, default='None')
    parcel_number = models.PositiveIntegerField(null=True, blank=True)
    zoning = models.CharField(max_length=10, null=True, blank=True, default="NA")
    new_construction = models.CharField(max_length = 10, default="No", choices=yes_no)
    major_remodel_year = models.PositiveIntegerField(null=True, blank=True, validators = [ MaxValueValidator(2020)])


    # Property Utilities
    sewer_options = (
        ('public sewer', 'public sewer'),
        ('septic system', 'septic system')
    )

    sewer_info = models.CharField(max_length=50, choices=sewer_options, default='public sewer')
    HOA_info = models.CharField(max_length = 200, default="No HOA")
    utilities = models.TextField(null=True)
    green_energy = models.TextField(default="No green energy utilities")


    #MLS Information

    status_options = (
        ('coming soon', 'coming soon'),
        ('active', 'active'),
        ('contingent', 'contingent'),
        ('pending', 'pending'),
        ('closed', 'closed'),
        ('expired', 'expired'),
        ('canceled', 'canceled'),
        ('withdrawn', 'withdrawn')
    )

    listing_id = models.CharField(max_length=50, null=True)
    mls_status = models.CharField(max_length=30, choices=status_options, default='active')

    


    def __str__(self):  
        return self.address.address
    
    class Meta:
        db_table = "Home"

