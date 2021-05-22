from abstract import abstract_item

class Central_AC(abstract_item):

    @property
    def item_id(self):
        return "cac"

    @property
    def item_name(self):
        return "Central AC"

    @property
    def price(self):
        return 1399.99

    @property
    def item_count(self):
        return 0

    @property
    def total_price(self):
        return 0

    def pricing_rule(self, list_obj):
        self.total_price = self.item_count * self.price
        if self.item_count > 0:
            for i in list_obj:
                if i.item_id == "mch" and i.item_count > 0:
                    if self.item_count > i.item_count:
                        i.item_count = 0
                    else:
                        i.item_count = i.item_count - self.item_count
        return self.total_price