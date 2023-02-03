from sqlalchemy import select, insert, and_, desc

from data_base.models.product_model import Product


class ProductTblWorker(Product):

    @staticmethod
    async def add(product: dict, local_session):
        """

        """
        add_product_query = insert(Product).values(
            product
        )
        await local_session.execute(add_product_query)

    @staticmethod
    async def get_all(local_session,
                      name: str = None,
                      manufacturer: str = None,
                      price_min: int = None,
                      price_max: int = None,
                      sorting: str = None) -> list:

        query = select(Product)
        if name:
            query = query. \
                where(and_(Product.name == str(name)))
        if manufacturer:
            query = query. \
                where(and_(Product.manufacturer == str(manufacturer)))
        if price_min:
            query = query. \
                where(and_(Product.price >= int(price_min)))
        if price_max:
            query = query. \
                where(and_(Product.price <= int(price_max)))
        match sorting:
            case "price_up":
                query = query.order_by(Product.price)
            case "price_down":
                query = query.order_by(-Product.price)
            case "name_up":
                query = query.order_by(Product.name)
            case "name_down":
                query = query.order_by(desc(Product.name))
            case _:
                pass

        result = await local_session.execute(query)
        products = result.scalars().all()
        return products

    @staticmethod
    async def get_by_id(product_id: int, local_session):
        """

        """
        query = select(Product).where(and_(Product.id == int(product_id)))

        result = await local_session.execute(query)
        product = result.scalars().first()

        return product
