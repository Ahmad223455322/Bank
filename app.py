from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

from model import db, seedData, Customer

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Ahmad123.@localhost/Bank'
db.app = app
db.init_app(app)
migrate = Migrate(app,db)
 
 

@app.route("/", methods=['GET', 'POST'])
def startpage():
    #trendingCategories = Category.query.all() trendingCategories=trendingCategories
    return render_template("loggain.html")

@app.route("/loggain", methods=['GET', 'POST'])
def loggain():
    databas = Customer.query.all()
    #trendingCategories = Category.query.all() trendingCategories=trendingCategories
    return render_template("index.html", databas= databas)

@app.route("/category/<id>")
def category(id):
    products = Product.query.all()
    return render_template("category.html", products=products)


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    
    app.run()
    seedData(db)

