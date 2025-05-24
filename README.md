# personal-finance-tracker-mvp
A simple, Gen Z-focused personal finance tracker MVP to manage budgets, track UPI-based transactions, and set savings goals.
# 💸 Personal Finance Tracker (MVP)

A Gen Z-focused personal finance tracker MVP that helps users manage budgets, monitor UPI-based expenses, and set & track savings goals — all with simple charts and category-wise breakdowns.

---

## 📱 Wireframe Preview

![Wireframes](![wireframe](https://github.com/user-attachments/assets/21303524-66a8-4ffe-8915-1678df582365)


---

## 🧩 Features

- ✅ User sign-up/login
- ✅ Set monthly budget by category (Food, Shopping, etc.)
- ✅ Track daily expenses from services like Swiggy, Zomato, Amazon
- ✅ Visual breakdown with pie chart and insights bar graph
- ✅ Create and track savings goals

---

## 🔧 Tech Stack

- **Frontend**: Figma (wireframes)
- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Deployment**: (To be added)
- **Version Control**: Git + GitHub

---

## 🗂 Project Structure
personal-finance-tracker-mvp/
├── backend/
│ ├── app.py # Main Flask app
│ ├── db_config.py # Database connection config
│ ├── requirements.txt # Python dependencies
│ └── README.md # Backend-specific instructions
├── design/
│ └── wireframes.png # Figma wireframe screenshot
├── docs/
│ └── product_spec.md # Product spec & functional doc
├── .gitignore
└── README.md # This file



---

## ⚙️ Installation (for local testing)

```bash
git clone https://github.com/your-username/personal-finance-tracker-mvp.git
cd personal-finance-tracker-mvp/backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py


🚀 Usage
Start the Flask server

Use Postman or a simple HTML form (later React frontend) to interact with APIs

Add expenses, create budgets, and view category breakdown

📈 Future Enhancements
UPI transaction parsing using SMS or email scraping

User dashboard frontend in React Native or Flutter

Savings goal progress visualizations

Firebase or Supabase for auth & analytics

Mobile PWA version

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.
