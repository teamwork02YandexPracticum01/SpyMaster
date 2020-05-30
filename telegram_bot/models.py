import peewee
from playhouse.sqlite_ext import JSONField

from telegram_bot.db_inizialization import database_proxy


class BaseTable(peewee.Model):
    class Meta:
        database = database_proxy


class UserState(BaseTable):
    """Состояние пользователя внутри сценария."""
    user_id = peewee.CharField(unique=True)
    scenario_name = peewee.CharField
    step_name = peewee.CharField
    context = JSONField()