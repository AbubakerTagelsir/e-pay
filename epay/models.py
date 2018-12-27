from django.db import models

class User(models.Model):
	GENDER_TYPE = (
        ("M", "Male"),
        ("F", "Female")
    )
	name = models.CharField()
	phone = models.CharField()
	address = models.TextField()
	gender = models.CharField(choices=GENDER_TYPE)

class Card(models.Model):
	number = models.CharField(max_length=100)
	balance = models.FloatField()
	user = models.ForiegnKey('User')
	bank = models.ForiegnKey('Bank')



class Transaction(models.Model):
	amount = models.FloatField()
	card_from = models.ForiegnKey('Card')
	date = models.DateTimeField(auto_now=True)


class TelecomTrans(object):
	"""docstring for TelecomTrans"""
	phone_number = models.CharField()
	company = models.ForiegnKey('TelecomBrand')
	service_fees = models.FloatField()


class CardTrans(object):
	"""docstring for CardTrans"""
	card_to = models.ForiegnKey('Card')
	service_fees = models.FloatField()
	

class ElectricityTrans(object):
	"""docstring for ElectricityTrans"""
	meter_no = models.CharField()
	service_fees = models.FloatField()
	# elect_amount = 
	# water_fees =
	
		
class TelecomBrand(object):
	"""docstring for TelecomBrand"""
	name = models.CharField()
	logo = models.ImageField()
	
		
class Bank(object):
	"""docstring for Bank"""
	name = models.CharField()
		