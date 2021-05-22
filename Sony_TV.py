from abstract import abstract_item

class Sony_TV(abstract_item):

    @property
    def item_id(self):
        return "stv"

    @property
    def item_name(self):
        return "Sony TV"

    @property
    def price(self):
        return 549.99

    @property
    def item_count(self):
        return 0

    @property
    def total_price(self):
        return 0

    def pricing_rule(self, list_obj):
        if self.item_count > 4:
            self.total_price = self.item_count * 499.99
        else:
            self.total_price = self.item_count * self.price
        return self.total_price