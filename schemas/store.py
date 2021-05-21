from start.ma import ma
from start.models.store import StoreModel
from start.models.item import ItemModel


class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemModel, many=True)
    class Meta:
        model = StoreModel
        dump_only = ("id",)
        include_fk = True
