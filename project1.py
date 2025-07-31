#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Bill Generation
catalog = {
    "Fruits": {"Apple": 30, "Banana": 10, "Mango": 50},
    "Vegetables": {"Potato": 20, "Onion": 25, "Tomato": 30},
    "Snacks": {"Chips": 15, "Cookies": 25, "Chocolate": 40}
}

cart = {}

# Show available products
def show_catalog():
    print("\n=== Product Catalog ===")
    for category, items in catalog.items():
        print(f"\n-- {category} --")
        for product, price in items.items():
            print(f"{product} - ₹{price}")

# Add product to cart
def add_to_cart(product_name, quantity):
    for category in catalog:
        if product_name in catalog[category]:
            price = catalog[category][product_name]
            if product_name in cart:
                cart[product_name]["quantity"] += quantity
                cart[product_name]["total_price"] += price * quantity
            else:
                cart[product_name] = {
                    "price": price,
                    "quantity": quantity,
                    "total_price": price * quantity
                }
            print(f"{quantity} x {product_name} added to cart.")
            return
    print("Product not found!")

# Display the final bill
def generate_bill():
    print("\n===== FINAL BILL =====")
    grand_total = 0
    for item, details in cart.items():
        print(f"{item} - ₹{details['price']} x {details['quantity']} = ₹{details['total_price']}")
        grand_total += details['total_price']
    print(f"Total Amount: ₹{grand_total}")
    print("=======================")

# Main Program
print("======WELCOME TO BILL SIMULATOR======")
while True:
    print("\n1. Show Catalog")
    print("2. Add Product to Cart")
    print("3. Generate Bill & Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_catalog()
    elif choice == '2':
        pname = input("Enter product name: ").strip()
        qty = int(input("Enter quantity: "))
        add_to_cart(pname, qty)
    elif choice == '3':
        generate_bill()
        break
    else:
        print("Invalid choice.")


# In[ ]:




