from start.ma import ma
from start.models.item import ItemModel
from start.models.store import StoreModel


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_only = ("store",)
        dump_only = ("id",)
        include_fk = True
