'''company.py'''
from peewee import Model, MySQLDatabase, AutoField, CharField, \
    DateTimeField, ForeignKeyField, BooleanField, DateField,  IntegerField

db =MySQLDatabase('two', user='root', password= 'root', host ='localhost', port=3306)

class BaseModel(Model):
    ''' Базовый класс '''
    class Meta:
        ''' Класс '''
        database = db

class Partners(BaseModel):
    ''' Партнеры '''
    id = AutoField()
    type = CharField()
    name_company = CharField()
    adress = CharField()
    TIN = IntegerField()
    Full_name = CharField()
    phone = CharField()
    email = CharField()
    logo = CharField()
    rating = IntegerField()
    sales_points = CharField()
    History = CharField()

class Menegers(BaseModel):
    ''' Менеджеры '''
    id = AutoField()
    seartch = CharField()
    name = CharField()
    password = CharField()
    rating = IntegerField()
    aplication = CharField(null = True)
    offers = CharField(null = True)

class Bid(BaseModel):
    ''' Заявки '''
    id = AutoField()
    price = IntegerField()
    data = DateField()
    quantity = IntegerField()
    data_insert = DateTimeField()
