from abc import abstractproperty, abstractmethod

class abstract_item():
    def __init__(self):
        pass

    @abstractproperty
    def item_id(self):
        pass

    @abstractproperty
    def item_name(self):
        pass

    @abstractproperty
    def item_price(self):
        pass

    @abstractproperty
    def item_count(self):
        pass

    @abstractproperty
    def total_price(self):
        pass

    @abstractmethod
    def pricing_rules(self):
        pass