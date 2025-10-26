class VendingMachine():
    def __init__(self, items, money):
        self.items = items
        self.money = money

    def vend(self, selection, item_money):
        selection = selection.upper()
        selected_item = None
        
        for item in self.items:
            if item['code'].upper() == selection:
                selected_item = item
                break
                
        if selected_item is None:
            return f"Invalid selection! : Money in vending machine = {self.money:.2f}"
        
        if selected_item['quantity'] == 0:
            return f"{selected_item['name']}: Out of stock!"
        
        if item_money < selected_item['price']:
            return "Not enough money!"
        
        change = item_money - selected_item['price']
        selected_item['quantity'] -= 1
        self.money += selected_item['price']
        if change == 0:
            return f"Vending {selected_item['name']}"
        
        return f"Vending {selected_item['name']} with {change:.2f} change."
