# 🧮 Sales Data Automation Suite

**A Python-powered automation pipeline that cleans, merges, and summarizes multi-branch sales data — automatically generating weekly reports and sending them via email.**

This project demonstrates practical **data engineering and automation skills** often required in business analytics and data science roles.  
It reflects a real-world workflow for companies managing sales data from multiple branches or sources.

---

## 🚀 Key Features

✅ **Automatic Data Cleaning** — Handles missing values, renames inconsistent columns, removes duplicates.  
✅ **Merging Multiple Sources** — Combines all branch-level sales files into one unified dataset.  
✅ **Summary Report Generation** — Produces Excel summaries and visual charts of key KPIs.  
✅ **Email Notification** — Sends weekly reports automatically to stakeholders.  
✅ **Task Scheduling** — Uses Python’s `schedule` module to run the pipeline weekly.  
✅ **Modular Architecture** — Each component (cleaning, merging, reporting, emailing) is isolated and reusable.

---

## 🧠 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3.9+ |
| **Libraries** | `pandas`, `matplotlib`, `schedule`, `smtplib`, `email` |
| **Automation** | Cron (Linux) / Task Scheduler (Windows) |
| **Optional UI** | Streamlit (planned extension) |

---

## 🗂️ Project Structure

```

sales-automation-suite/
│
├── data/
│   ├── raw/               # Input files (BranchA.xlsx, BranchB.csv, etc.)
│   ├── cleaned/           # Intermediate cleaned data
│   └── reports/           # Generated reports and charts
│
├── scripts/
│   ├── **init**.py
│   ├── clean_data.py      # Cleans and standardizes raw data
│   ├── merge_data.py      # Merges all cleaned files
│   ├── generate_report.py # Summarizes KPIs and plots charts
│   ├── email_report.py    # Sends the final report via email
│   └── scheduler.py       # Runs the pipeline weekly
│
├── pipeline.py             # Main orchestrator for the suite
├── requirements.txt
├── README.md
└── demo.mp4                # Optional demo video

````

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-automation-suite.git
cd sales-automation-suite
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Linux / macOS
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Raw Sales Files

Place your Excel/CSV files inside the `data/raw` folder.
Example:

```
data/raw/
├── Riyadh_Branch.xlsx
├── Jeddah_Branch.csv
└── Dammam_Branch.xlsx
```

---

## ▶️ Running the Pipeline

Run the entire automation with:

```bash
python pipeline.py
```

**What happens:**

1. Cleans all files in `data/raw/`
2. Merges them into one dataset
3. Generates summary Excel & chart
4. Emails the report automatically

---

## 📅 Scheduling (Optional)

To automate weekly execution:

### On Windows

Use **Task Scheduler** → create a new task:

```bash
python path\to\pipeline.py
```

### On Linux / macOS

Use **cron**:

```bash
crontab -e
# Run every Monday at 8 AM
0 8 * * 1 /usr/bin/python3 /path/to/pipeline.py
```

Alternatively, use the built-in Python scheduler:

```bash
python scripts/scheduler.py
```

---

## ✉️ Email Configuration

Edit `scripts/email_report.py`:

```python
sender = "your_email@example.com"
password = "YOUR_APP_PASSWORD"
recipient = "manager@example.com"
```

> ⚠️ Use an **App Password** (not your main email password).
> For Gmail: [Generate App Passwords](https://myaccount.google.com/apppasswords)

You can also store credentials safely in a `.env` file:

```
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password
```

And load it with `python-dotenv`.

---

## 📈 Example Output

**Weekly Summary (Excel):**

| Total Sales | Top Branch | Top Product | Report Date |
| ----------- | ---------- | ----------- | ----------- |
| 120,540 SAR | Jeddah     | Product A   | 2025-10-05  |

**Bar Chart:**
*(Sales by Branch — auto-generated)*
![Sales Chart](data/reports/sales_chart_sample.png)

---

## 🎥 Demo Video

> ▶️ [Watch Demo](src/assets/demo.mp4)

---

## 💡 Future Enhancements

* 🔹 Add Streamlit dashboard for visual uploads and downloads
* 🔹 Integrate Google Sheets or Drive API for cloud storage
* 🔹 Auto-refresh linked Power BI dashboards via API
* 🔹 Add logging and error tracking for production use

---

## 👨‍💻 Author

**Ahmed I** — Data Scientist | Automation Builder | AI Enthusiast
📍 Based in KSA 🇸🇦
📫 [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) • [GitHub](https://github.com/YOUR_USERNAME)

---

## 🏁 License

This project is open-source under the **MIT License** — feel free to use, adapt, and improve it for your own automation workflows.

```