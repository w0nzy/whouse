from pydantic import BaseModel

class api_ItemIDModel(BaseModel):
    id: int
    category_name: str
    category_description: str

class api_SupplierModel(BaseModel):
    id: int
    supplier_name: str

class api_ItemModel(BaseModel):
    id: int
    item_name: str
    item_category_id: int
    item_barcode: str
    item_batch: str
    item_movement: bool
