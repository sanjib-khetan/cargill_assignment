from abstract import abstract_item

class Charger(abstract_item):

    @property
    def item_id(self):
        return "mch"

    @property
    def item_name(self):
        return "Charger"

    @property
    def price(self):
        return 30.00

    @property
    def item_count(self):
        return 0

    @property
    def total_price(self):
        return 0

    def pricing_rule(self, list_obj):
        self.total_price = self.item_count * self.price
        return self.total_price