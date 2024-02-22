class Product():

    def __init__(self, product_id=None, product_type_id=None, product_code=None, 
                 product_brand=None, product_name=None, 
                 product_creation_date=None, 
                 product_update_date=None, product_last_user=None) -> None:
        
        self.product_id = product_id
        self.product_code = product_code
        self.product_brand = product_brand
        self.product_name = product_name
        self.product_type_id = product_type_id
        self.product_creation_date = product_creation_date
        self.product_update_date = product_update_date
        self.product_last_user = product_last_user

    def to_JSON(self):
        return {
            'PRODUCT_ID': self.product_id,
            'PRODUCT_CODE': self.product_code,
            'PRODUCT_BRAND': self.product_brand,
            'PRODUCT_NAME': self.product_name,
            'PRODUCT_TYPE_ID': self.product_type_id,
            'PRODUCT_CREATION_DATE': self.product_creation_date,
            'PRODUCT_UPDATE_DATE': self.product_update_date,
            'PRODUCT_LAST_USER': self.product_last_user
        }
