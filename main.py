from Sony_TV import Sony_TV
from Central_AC import Central_AC
from Nike_Shoe import Nike_Shoes
from Charger import Charger

class Checkout():

    def __init__(self, list_item_obj):
        self.total_price = 0
        self.list_item_obj = list_item_obj
        self.list_obj = self.get_obj_list()
        self.get_obj_count(list_item_obj, self.list_obj)

    def get_obj_list(self):
        sony_obj = Sony_TV()
        nike_obj = Nike_Shoes()
        central_ac_obj = Central_AC()
        charger_obj = Charger()
        return [sony_obj, nike_obj, central_ac_obj, charger_obj]

    def get_obj_count(self, list_item_obj, list_obj):
        for itm in list_item_obj:
            for obj_itm in list_obj:
                if itm.item_id == obj_itm.item_id:
                    obj_itm.item_count += 1

    def get_total_price(self):
        for obj in self.list_obj:
            self.total_price += obj.pricing_rule(self.list_obj)
        return self.total_price

class item():
    def __init__(self, item_id):
        self.item_id = item_id

if __name__ == "__main__":

    i1 = item("nsh")
    i2 = item("stv")
    i3 = item("stv")
    i4 = item("nsh")
    i5 = item("stv")
    i6 = item("stv")
    i7 = item("stv")
    check_out = Checkout([i1, i2, i3, i4, i5, i6, i7])
    print(check_out.get_total_price())



