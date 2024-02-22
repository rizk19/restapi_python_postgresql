from database.db import get_connection
from .entities.Product import Product


class ProductModel():

    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT PRODUCT_TYPE_ID, PRODUCT_BATCH_NUMBER, PRODUCT_NETTO, PRODUCT_MEASUREMENT_UNIT_ID, PRODUCT_COLOUR_ID, PRODUCT_RAW_MATERIAL_TRADENAME, PRODUCT_RAW_MATERIAL_INCHINAME, PRODUCT_RAW_MATERIAL_INCHINAME_PERCENTAGE, PRODUCT_RAW_MATERIAL_FUNCTION, PRODUCT_RAW_MATERIAL_EXPIRED_DATE, PRODUCT_RAW_MATERIAL_HALAL_ID, PRODUCT_PACKAGING_ITEM, PRODUCT_PACKAGING_ITEM_PART_ID, PRODUCT_FINISH_GOODS_NAME, PRODUCT_FINISH_GOODS_BPOM_NUMBER, PRODUCT_FINISH_GOODS_BPOM_EXPIRED_DATE, PRODUCT_FINISH_GOODS_HALAL_CERTIFICATION_NUMBER, PRODUCT_FINISH_GOODS_SUBSTANCE_ID, PRODUCT_PACKAGING_ITEM_FULLNAME, PRODUCT_CODE, PRODUCT_ID, PRODUCT_FINISH_GOODS_BRAND, PRODUCT_NAME, PRODUCT_PACKAGING_TYPE, PRODUCT_CREATION_DATE, PRODUCT_UPDATE_DATE, PRODUCT_LAST_USER FROM PRODUCTS ORDER BY PRODUCT_NAME ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    product = Product(
                        product_id=row[0],
                        product_type_id=row[1],
                        product_code=row[2],
                        product_brand=row[3],
                        product_name=row[4],
                        product_creation_date=row[5],
                        product_update_date=row[6],
                        product_last_user=row[7]
                    )
                    products.append(product.to_JSON())

            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_product(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT PRODUCT_TYPE_ID, PRODUCT_BATCH_NUMBER, PRODUCT_NETTO, PRODUCT_MEASUREMENT_UNIT_ID, PRODUCT_COLOUR_ID, PRODUCT_RAW_MATERIAL_TRADENAME, PRODUCT_RAW_MATERIAL_INCHINAME, PRODUCT_RAW_MATERIAL_INCHINAME_PERCENTAGE, PRODUCT_RAW_MATERIAL_FUNCTION, PRODUCT_RAW_MATERIAL_EXPIRED_DATE, PRODUCT_RAW_MATERIAL_HALAL_ID, PRODUCT_PACKAGING_ITEM, PRODUCT_PACKAGING_ITEM_PART_ID, PRODUCT_FINISH_GOODS_NAME, PRODUCT_FINISH_GOODS_BPOM_NUMBER, PRODUCT_FINISH_GOODS_BPOM_EXPIRED_DATE, PRODUCT_FINISH_GOODS_HALAL_CERTIFICATION_NUMBER, PRODUCT_FINISH_GOODS_SUBSTANCE_ID, PRODUCT_PACKAGING_ITEM_FULLNAME, PRODUCT_CODE, PRODUCT_ID, PRODUCT_FINISH_GOODS_BRAND, PRODUCT_NAME, PRODUCT_PACKAGING_TYPE, PRODUCT_CREATION_DATE, PRODUCT_UPDATE_DATE, PRODUCT_LAST_USER FROM PRODUCTS WHERE PRODUCT_ID = %s", (id,))
                row = cursor.fetchone()

                product = None
                if row != None:
                    product = Product(
                        product_id=row[0],
                        product_type_id=row[1],
                        product_code=row[2],
                        product_brand=row[3],
                        product_name=row[4],
                        product_creation_date=row[5],
                        product_update_date=row[6],
                        product_last_user=row[7]
                    )
                    product = product.to_JSON()

            connection.close()
            return product
        except Exception as ex:
            raise Exception(ex)

    # @classmethod
    # def add_product(self, movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("""INSERT INTO movie (id, title, duration, released) 
    #                             VALUES (%s, %s, %s, %s)""", (movie.id, movie.title, movie.duration, movie.released))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)

    # @classmethod
    # def update_product(self, movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("""UPDATE movie SET title = %s, duration = %s, released = %s 
    #                             WHERE id = %s""", (movie.title, movie.duration, movie.released, movie.id))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)

    # @classmethod
    # def delete_product(self, movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("DELETE FROM movie WHERE id = %s", (movie.id,))
    #             affected_rows = cursor.rowcount
    #             connection.commit()

    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)
