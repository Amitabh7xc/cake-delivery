from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample cake data
cakes = [
    {"id": 1, "name": "Chocolate", "price": 500, "description": "A decadent chocolate cake layered with rich mocha ganache, topped with chocolate curls and a hint of espresso for true chocolate lovers.", "image": "cake1.jpg"},
    {"id": 2, "name": "Vanilla", "price": 400, "description": "A classic vanilla sponge cake, light and fluffy, filled with creamy vanilla bean frosting and finished with delicate sprinkles.", "image": "cake2.jpg"},
    {"id": 3, "name": "Red Velvet", "price": 600, "description": "A luxurious red velvet cake with a subtle cocoa flavor, layered with smooth cream cheese frosting and garnished with red velvet crumbs.", "image": "cake3.jpg"},
]

# Sample order data
orders = []

@app.route("/")
def index():
    return render_template("index.html", cakes=cakes)

@app.route("/cake/<int:cake_id>")
def cake(cake_id):
    cake = next((cake for cake in cakes if cake["id"] == cake_id), None)
    if cake is None:
        return redirect(url_for("index"))
    return render_template("cake.html", cake=cake)

@app.route("/order/<int:cake_id>", methods=["GET", "POST"])
def order(cake_id):
    cake = next((cake for cake in cakes if cake["id"] == cake_id), None)
    if cake is None:
        return redirect(url_for("index"))

    if request.method == "POST":
        customer_name = request.form["customer_name"]
        address = request.form["address"]
        phone_number = request.form["phone_number"]
        orders.append({"cake": cake, "customer_name": customer_name, "address": address, "phone_number": phone_number})
        return redirect(url_for("confirmation"))

    return render_template("order.html", cake=cake)

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)