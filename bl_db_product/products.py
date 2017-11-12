from .database import DataBase



class Product(DataBase):
  def __init__(self):
    super().__init__()
    self.products = self.db.products

  def add_product(self, data):
    res = self.products.insert({"bok": data})
    return str(res)
