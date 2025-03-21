from pyDatalog import pyDatalog

# Initialize the PyDatalog environment
pyDatalog.create_terms('Item, Price, Quantity, ReorderPoint, StockLevel, TotalInventoryValue, Sell, Restock, TotalValue, NewQuantity')

# Define an inventory item with its quantity, price, and reorder point
+Item('laptop', 10, 1000, 3)
+Item('phone', 15, 500, 5)
+Item('headphones', 20, 100, 10)

# Rule to track stock level of an item
StockLevel(Item, Quantity) <= Item(Item, Quantity, _, _)

# Rule to calculate total inventory value
TotalValue(Item, Value) <= (Item(Item, Quantity, Price, _)) & (Value == Quantity * Price)

# Rule to get total inventory value
TotalInventoryValue(Sum) <= pyDatalog.sum_(Value for Item, Value in TotalValue(Item, Value))

# Rule to simulate a sale (decrease stock)
Sell(Item, SoldQty) <= (Item(Item, Quantity, Price, ReorderPoint)) & (NewQuantity == Quantity - SoldQty) & \
                        (NewQuantity >= 0) & (Item.retract(Item(Item, _, _, _))) & \
                        (Item(Item, NewQuantity, Price, ReorderPoint))

# Rule to simulate restocking (increase stock)
Restock(Item, RestockQty) <= (Item(Item, Quantity, Price, ReorderPoint)) & (NewQuantity == Quantity + RestockQty) & \
                            (Item.retract(Item(Item, _, _, _))) & \
                            (Item(Item, NewQuantity, Price, ReorderPoint))

# Rule to check if an item needs restocking (below reorder point)
ReorderPoint(Item, ReorderQty) <= (Item(Item, Quantity, _, ReorderPoint)) & \
                                  (Quantity < ReorderPoint) & (ReorderQty == ReorderPoint - Quantity)

# Queries
print("Initial stock levels:")
print(pyDatalog.ask('StockLevel(Item, Quantity)'))

print("\nInitial total inventory value:")
print(pyDatalog.ask('TotalInventoryValue(Sum)'))

# Simulate a sale of 2 laptops
print("\nSimulating sale of 2 laptops:")
Sell('laptop', 2)
print(pyDatalog.ask('StockLevel(Item, Quantity)'))

# Simulate restocking of 5 phones
print("\nSimulating restocking of 5 phones:")
Restock('phone', 5)
print(pyDatalog.ask('StockLevel(Item, Quantity)'))

# Check if any items need restocking
print("\nItems that need restocking:")
print(pyDatalog.ask('ReorderPoint(Item, ReorderQty)'))

# Final total inventory value
print("\nFinal total inventory value:")
print(pyDatalog.ask('TotalInventoryValue(Sum)'))
