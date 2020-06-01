import peewee
from playhouse.sqlite_ext import JSONField

from telegram_bot.db_inizialization import database_proxy


class BaseTable(peewee.Model):
    """Таблица от которой будут наследованы все модели."""

    class Meta:
        database = database_proxy


class CommandHandler(BaseTable):
    """Состояние пользователя внутри сценария."""
    user_id = peewee.CharField(unique=True)
    scenario_name = peewee.CharField
    step_name = peewee.CharField
    context = JSONField()


class User(BaseTable):
    """Цели для слежки для каждого user"""
    user_id = peewee.CharField(unique=True)
    max_targets = peewee.IntegerField
    targets = peewee.ValuesList
