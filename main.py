'''ТЕСТОВЫЙ ФАЙЛ'''
from peewee import Model, MySQLDatabase, AutoField, IntegerField, CharField, \
    DateTimeField

db = MySQLDatabase('two', user ='root', password ='root', host ='localhost', port=3306)

class BaseModel(Model):
    ''' БАЗОВЫЙ КЛАСС'''
    class Meta:
        '''Класс мета'''
        database = db

class Main(BaseModel):
    '''Класс'''
    id = AutoField()
    number = IntegerField()
    text = CharField()
    data = DateTimeField()


db.connect()
db.create_tables([Main], safe=True)
db.close()
