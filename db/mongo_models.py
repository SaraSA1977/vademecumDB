# class ProductImage:
#     def __init__(self, **data):
#         self._id = data.get("_id")
#         self.product_id = data.get("product_id")
#         self.name = data.get("name")
#         self.image_url = data.get("image_url")
#         self.image_type = data.get("image_type")
#         self.created_at = data.get("created_at")
#         self.updated_at = data.get("updated_at")
 
#     def to_dict(self):
#         return {
#             "id": str(self._id) if self._id else None,
#             "product_id": self.product_id,
#             "name": self.name,
#             "image_url": self.image_url,
#             "image_type": self.image_type,
#             "created_at": self.created_at,
#             "updated_at": self.updated_at
#         }