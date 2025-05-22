from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from db_config import db

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class SavingGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goal_name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)

# Routes

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    category = data.get('category')
    description = data.get('description', '')

    expense = Expense(user_id=user_id, amount=amount, category=category, description=description)
    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Expense added"}), 201

@app.route('/budgets', methods=['POST'])
def set_budget():
    data = request.get_json()
    user_id = data.get('user_id')
    category = data.get('category')
    amount = data.get('amount')

    budget = Budget.query.filter_by(user_id=user_id, category=category).first()
    if budget:
        budget.amount = amount
    else:
        budget = Budget(user_id=user_id, category=category, amount=amount)
        db.session.add(budget)
    db.session.commit()

    return jsonify({"message": "Budget set"}), 201

@app.route('/saving-goals', methods=['POST'])
def set_saving_goal():
    data = request.get_json()
    user_id = data.get('user_id')
    goal_name = data.get('goal_name')
    target_amount = data.get('target_amount')

    goal = SavingGoal(user_id=user_id, goal_name=goal_name, target_amount=target_amount)
    db.session.add(goal)
    db.session.commit()

    return jsonify({"message": "Saving goal created"}), 201

@app.route('/dashboard/<int:user_id>', methods=['GET'])
def dashboard(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    budgets = Budget.query.filter_by(user_id=user_id).all()
    saving_goals = SavingGoal.query.filter_by(user_id=user_id).all()

    expenses_list = [{"amount": e.amount, "category": e.category, "description": e.description} for e in expenses]
    budgets_list = [{"category": b.category, "amount": b.amount} for b in budgets]
    goals_list = [{"goal_name": g.goal_name, "target_amount": g.target_amount, "current_amount": g.current_amount} for g in saving_goals]

    return jsonify({
        "expenses": expenses_list,
        "budgets": budgets_list,
        "saving_goals": goals_list
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
