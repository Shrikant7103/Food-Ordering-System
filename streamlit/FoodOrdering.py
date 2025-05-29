import streamlit as st

# Define the menu globally
menu = {
    'Pasta': 250,
    'Pizza': 300,
    'Salad': 150
}

st.title("🍽️ Welcome to Our Restaurant!")

st.header("Menu")
for item, price in menu.items():
    st.write(f"**{item}**: ₹{price}")

st.header("Place Your Order")
selected_items = st.multiselect("Select the items you want to order:", list(menu.keys()))

if selected_items:
    order_total = sum(menu[item] for item in selected_items)
    st.subheader("Order Summary")
    for item in selected_items:
        st.write(f"{item}: ₹{menu[item]}")
    st.write(f"**Total Amount: ₹{order_total}**")
else:
    st.write("Please select at least one item to place an order.")
