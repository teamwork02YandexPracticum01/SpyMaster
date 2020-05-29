import peewee

database_proxy = peewee.DatabaseProxy()


class BaseTable(peewee.Model):
    class Meta:
        database = database_proxy



