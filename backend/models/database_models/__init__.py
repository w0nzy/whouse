import logging
from sqlalchemy import (String,Integer,ForeignKey,BOOLEAN)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.orm import relationship


class model_base(DeclarativeBase):
    pass

class db_ItemID(model_base):
    __tablename__ = "item_categories"
    id: Mapped[int] = mapped_column(
        primary_key = True,
        autoincrement = True
    )

    category_name: Mapped[str] = mapped_column(String(10))
    category_description: Mapped[str] = mapped_column(String(30))

class db_SupplierTableModel(model_base):
    __tablename__ = "item_suppliers"
    id: Mapped[int] = mapped_column(
        primary_key = True,
        autoincrement = True)
    supplier_name: Mapped[str] = mapped_column(String(30),nullable = False)

class db_ItemTableModel(model_base):
    """

    - * - ürünler hakkında
   * ürün id
   * ürün ismi
   * ürün kategori id 
   * ürün barkodu
   * ürün lot
   * ürün hareketi olmuş mu olmamış mı 
   """
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(
        primary_key = True,
        autoincrement = True
    )
    item_name: Mapped[str] = mapped_column(String(40),nullable=False)
    item_category_id: Mapped[int] = mapped_column(ForeignKey("item_categories.id"))
    item_barcode: Mapped[str] = mapped_column(String(20))
    item_batch: Mapped[str] = mapped_column(String(20))
    item_movement: Mapped[bool] = mapped_column(BOOLEAN)


def create_all_table(engine):
    for table in globals().values():
        if hasattr(table,"__tablename__"):
            table.metadata.create_all(engine,checkfirst = True)
            logging.info("Tablolar oluşturuluyor: %s" % (table.__tablename__))