import os
import logging
import pandas as pd
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# =========================
# LOGGING SETUP
# =========================
logging.basicConfig(
    filename="actions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("✅ actions.py loaded successfully")


# =========================
# SAMPLE DATAFRAME
# =========================
sales_data = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"],
    "sales": [50000, 30000, 20000, 10000, 40000],
    "profit": [8000, 5000, 2000, 1500, 6000]
})


# =========================
# 1. TOTAL SALES
# =========================
class ActionTotalSales(Action):

    def name(self):
        return "action_total_sales"

    def run(self, dispatcher, tracker, domain):
        try:
            total = sales_data["sales"].sum()
            msg = f"📊 Total Sales: {total}"
            dispatcher.utter_message(text=msg)
            logging.info(msg)

        except Exception as e:
            dispatcher.utter_message(text="Error calculating total sales.")
            logging.error(str(e))

        return []


# =========================
# 2. AVERAGE SALES
# =========================
class ActionAverageSales(Action):

    def name(self):
        return "action_average_sales"

    def run(self, dispatcher, tracker, domain):
        try:
            avg = sales_data["sales"].mean()
            msg = f"📊 Average Sales: {avg:.2f}"
            dispatcher.utter_message(text=msg)
            logging.info(msg)

        except Exception as e:
            dispatcher.utter_message(text="Error calculating average sales.")
            logging.error(str(e))

        return []


# =========================
# 3. HIGHEST SALES
# =========================
class ActionHighestSales(Action):

    def name(self):
        return "action_highest_sales"

    def run(self, dispatcher, tracker, domain):
        try:
            row = sales_data.loc[sales_data["sales"].idxmax()]
            msg = f"🔥 Highest Sales: {row['product']} ({row['sales']})"
            dispatcher.utter_message(text=msg)
            logging.info(msg)

        except Exception as e:
            dispatcher.utter_message(text="Error finding highest sales.")
            logging.error(str(e))

        return []


# =========================
# 4. LOWEST SALES
# =========================
class ActionLowestSales(Action):

    def name(self):
        return "action_lowest_sales"

    def run(self, dispatcher, tracker, domain):
        try:
            row = sales_data.loc[sales_data["sales"].idxmin()]
            msg = f"📉 Lowest Sales: {row['product']} ({row['sales']})"
            dispatcher.utter_message(text=msg)
            logging.info(msg)

        except Exception as e:
            dispatcher.utter_message(text="Error finding lowest sales.")
            logging.error(str(e))

        return []


# =========================
# 5. PROFIT PERCENTAGE
# =========================
class ActionProfitPercentage(Action):

    def name(self):
        return "action_profit_percentage"

    def run(self, dispatcher, tracker, domain):
        try:
            sales_data["profit_percent"] = (sales_data["profit"] / sales_data["sales"]) * 100
            avg_profit = sales_data["profit_percent"].mean()

            msg = f"💰 Average Profit %: {avg_profit:.2f}%"
            dispatcher.utter_message(text=msg)
            logging.info(msg)

        except Exception as e:
            dispatcher.utter_message(text="Error calculating profit percentage.")
            logging.error(str(e))

        return []


# =========================
# 6. READ SALES CSV
# =========================
class ActionReadSalesCSV(Action):

    def name(self):
        return "action_read_sales_csv"

    def run(self, dispatcher, tracker, domain):
        try:
            df = pd.read_csv("data/sales.csv")
            total = df["sales"].sum()

            dispatcher.utter_message(text=f"📁 CSV loaded. Total Sales: {total}")
            logging.info("CSV loaded successfully")

        except FileNotFoundError:
            dispatcher.utter_message(text="❌ sales.csv file not found")
            logging.error("CSV file missing")

        return []


# =========================
# 7. READ EMPLOYEES EXCEL
# =========================
class ActionReadEmployeesExcel(Action):

    def name(self):
        return "action_read_employee_excel"

    def run(self, dispatcher, tracker, domain):
        try:
            df = pd.read_excel("data/employees.xlsx")

            total_employees = len(df)
            best_employee = df.loc[df["performance_score"].idxmax()]

            msg = f"👨‍💼 Employees: {total_employees}, Best: {best_employee['name']}"
            dispatcher.utter_message(text=msg)

            logging.info("Excel processed successfully")

        except FileNotFoundError:
            dispatcher.utter_message(text="❌ Excel file not found")
        except ValueError:
            dispatcher.utter_message(text="❌ Invalid Excel format")

        return []


# =========================
# 8. READ COMPLAINT JSON
# =========================
class ActionReadComplaints(Action):

    def name(self):
        return "action_read_complaints"

    def run(self, dispatcher, tracker, domain):
        try:
            with open("data/complaints.json") as f:
                data = json.load(f)

            complaints = [c["complaint"] for c in data]
            most_common = max(set(complaints), key=complaints.count)

            msg = f"⚠️ Most Common Complaint: {most_common}"
            dispatcher.utter_message(text=msg)

        except Exception as e:
            dispatcher.utter_message(text="Error reading complaints file")
            logging.error(str(e))

        return []


# =========================
# 9. TOP SELLING PRODUCT
# =========================
class ActionTopProduct(Action):

    def name(self):
        return "action_top_product"

    def run(self, dispatcher, tracker, domain):
        try:
            row = sales_data.loc[sales_data["sales"].idxmax()]
            dispatcher.utter_message(text=f"🏆 Top Product: {row['product']}")
        except Exception as e:
            logging.error(str(e))

        return []


# =========================
# 10. LEAST SELLING PRODUCT
# =========================
class ActionLeastProduct(Action):

    def name(self):
        return "action_least_product"

    def run(self, dispatcher, tracker, domain):
        try:
            row = sales_data.loc[sales_data["sales"].idxmin()]
            dispatcher.utter_message(text=f"📉 Least Product: {row['product']}")
        except Exception as e:
            logging.error(str(e))

        return []


# =========================
# 11. TOTAL EMPLOYEES
# =========================
class ActionTotalEmployees(Action):

    def name(self):
        return "action_total_employees"

    def run(self, dispatcher, tracker, domain):
        try:
            df = pd.read_excel("data/employees.xlsx")
            dispatcher.utter_message(text=f"👨‍💼 Total Employees: {len(df)}")
        except Exception as e:
            logging.error(str(e))

        return []


# =========================
# 12. BEST EMPLOYEE
# =========================
class ActionBestEmployee(Action):

    def name(self):
        return "action_best_employee"

    def run(self, dispatcher, tracker, domain):
        try:
            df = pd.read_excel("data/employees.xlsx")
            best = df.loc[df["performance_score"].idxmax()]
            dispatcher.utter_message(text=f"🏅 Best Employee: {best['name']}")
        except Exception as e:
            logging.error(str(e))

        return []