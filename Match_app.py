from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Citrus_group01.db'
db3 = SQLAlchemy(app)

class Customer_form(db3.Model):
    contact_id = db3.Column(db3.Integer, primary_key=True)
    full_name = db3.Column(db3.String(70), nullable=False)
    email = db3.Column(db3.String(100), nullable=False)
    phone = db3.Column(db3.Integer, default=0)
    budget = db3.Column(db3.Integer, default=0)
    monthly_cost = db3.Column(db3.Integer, default=0)
    real_estate_type = db3.Column(db3.String(100), nullable=False)
    floor = db3.Column(db3.String(100), nullable=True)
    square_m2 = db3.Column(db3.Integer, default=0)
    area =  db3.Column(db3.String(100), nullable=False)
    environment = db3.Column(db3.String(100), nullable=False)
    balcony = db3.Column(db3.Boolean)
    garden = db3.Column(db3.Boolean)
    pool = db3.Column(db3.Boolean)
    rent_out = db3.Column(db3.Boolean)
    when_to_buy = db3.Column(db3.Integer, default=0) 

@app.route('/', methods=['POST', 'GET'])

def insert():

    if request.method == 'POST':
        
        try:
            contact_id = request.form['contact_id']
            full_name = request.form['full_name']
            email = request.form['email']
            phone = request.form['phone']
            budget = request.form['budget']
            monthly_cost = request.form['monthly_cost']
            real_estate_type = request.form['real_estate_type']
            floor = request.form['floor']
            square_m2 = request.form['square_m2']
            area = request.form['area']
            environment = request.form['environment']
            balcony = request.form['balcony']
            garden = request.form['garden']
            pool = request.form['pool']
            rent_out = request.form['rent_out']
            when_to_buy = request.form['when_to_buy']

            data = [contact_id, full_name, email, phone, budget, monthly_cost, real_estate_type
            floor, square_m2, area, environment, balcony, garden, pool, rent_out, when_to_buy]

            db3.session.add(data)
            db3.session.commit()

            print data.id

        except:
            'there was a problem writing the the data to the database, check the injection keys'

    elif request.form[contact_id] == Customer_form.query.first(contact_id):
        return "customer contact ID already exists"

@app.route('/delete/<int:id>')
def delete(contact_id):
    contact_to_delete = Customer_form.query.get(contact_id)
    
    try:
        db3.session.delete(contact_to_delete)
        db3.session.commit()
        return print(contact_id 'deleted')

    except:
        return 'there was a problem deleting the contact_id'

if __name__ == "__main__":
    app.run(debug=True)
