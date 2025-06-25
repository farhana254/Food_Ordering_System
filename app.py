from flask import Flask, render_template, redirect, session, url_for
from datetime import datetime
import database

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def menu():
    items = database.get_food_items()
    return render_template('menu.html', items=items)

@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    cart = session.get('cart', [])
    cart.append(item_id)
    session['cart'] = cart
    return redirect(url_for('menu'))

@app.route('/cart')
def cart():
    cart_ids = session.get('cart', [])
    items = []

    for i in cart_ids:
        t = database.get_item_by_id(i)  # tuple: (id, name, price)
        if t:
            items.append({'id': t[0], 'name': t[1], 'price': t[2]})  # convert to dict

    return render_template('cart.html', items=items)

@app.route('/place_order')
def place_order():
    cart_ids = session.get('cart', [])
    if not cart_ids:
        return redirect(url_for('menu'))
    items_str = ','.join(map(str, cart_ids))
    database.save_order(items_str, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    session['cart'] = []
    return render_template('delivery_time.html')

@app.route('/order_history')
def order_history():
    orders = database.get_all_orders()
    return render_template('order_history.html', orders=orders)
    
if __name__ == '__main__':
    app.run(debug=True)
