from abstract import abstract_item

class Nike_Shoes(abstract_item):

    @property
    def item_id(self):
        return "nsh"

    @property
    def item_name(self):
        return "Nike Shoe"

    @property
    def price(self):
        return 109.50

    @property
    def item_count(self):
        return 0

    @property
    def total_price(self):
        return 0


    def pricing_rule(self, list_obj):
        self.total_price = (((self.item_count // 3) * 2) + (self.item_count % 3)) * self.price
        return self.total_price