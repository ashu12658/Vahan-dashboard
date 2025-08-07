# 🚀 Vehicle Registration Analytics Dashboard

An interactive dashboard to visualize and analyze **vehicle registration trends in India** using data from the **Vahan Dashboard**.

Built using **Streamlit**, the dashboard displays **Year-over-Year (YoY)** and **Quarter-over-Quarter (QoQ)** growth for:
- 📊 Vehicle types (2W / 3W / 4W)
- 🏭 Vehicle manufacturers (Hero, Bajaj, etc.)

---

## 📌 Objective

This project was developed as part of a **Backend Developer Internship** assignment with the aim of:
- Building a clean, investor-friendly dashboard
- Presenting key growth metrics to derive **investment insights**
- Practicing modular, scalable backend development in Python
---
## 📊 Features
- ✅ Vehicle-type wise YoY growth
- ✅ Manufacturer-wise YoY + QoQ growth
- ✅ Clean, responsive UI with Streamlit
- ✅ Sidebar filters: Year, Category, Manufacturer, Quarter
- ✅ Trend visualizations using Plotly
- ✅ Modular code with separate data processing scripts
- ✅ Ready for scraping, AI prediction & extension
---
## 📁 Folder Structure

├── dashboard/
│ └── app.py # Streamlit dashboard UI
│
├── utils/
│ └── qoq_clean.py # Script to clean & generate QoQ data
│
├── data/
│ ├── clean_data.csv # Vehicle type YoY data
│ ├── manufacturer_data.csv # Manufacturer-wise YoY data
│ └── qoq_data.csv # Manufacturer-wise QoQ data
│
├── monthly_data.csv # Raw monthly manufacturer data
├── requirements.txt # Project dependencies
└── README.md # You’re reading it


---

## ⚙️ Setup Instructions

1. **Clone the project**
```bash
git clone https://github.com/ashu12658/Vahan-dashboard.git
cd vahan-dashboard

pip install -r requirements.txt

python utils/qoq_clean.py

python utils/qoq_clean.py

🧠 Data Sources
📌 Vahan Dashboard (https://vahan.parivahan.gov.in/)

✅ Includes:

Monthly & yearly registrations

Manufacturer-wise data

2W / 3W / 4W breakdown

📈 Sample Investor Insights
🚀 Hero has shown consistent QoQ growth from Q1 2024 through 2025 — strong market stability.

📉 Bajaj dipped in Q1 2024 but recovered sharply in Q2 and beyond — possible rebound signal.

🛵 2-Wheelers dominate registration volumes — high-volume sector attractive for investors.

📹 Walkthrough Video
🎥 Watch the 5-minute demo
Covers usage, filters, graphs, and key insights

🔮 Future Enhancements
 Scrape live data from Vahan using Selenium or Playwright

 Integrate AI to forecast next quarter trends

 Export visualizations as PDF/Excel reports

 Add user login + saved insights for agents/investors

👨‍💻 Author
Ashish – Backend Developer (MERN Stack + Python)
📧 ashishghatol098@gmail.com
🌐 GitHub

📜 License
MIT License – Free to use with attribution.

🙌 Acknowledgements
Government of India – Vahan Dashboard

Streamlit, Pandas, Plotly

