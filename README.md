# 🤖 Rasa Chatbot Project (Tasks 30–51)

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Rasa](https://img.shields.io/badge/Rasa-Chatbot-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-darkblue?logo=pandas)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Project Overview

This project is an AI-powered chatbot built using **Rasa Open Source + Python**. It performs real-world business analytics such as sales analysis, employee performance tracking, complaint analysis, and file handling using CSV, Excel, and JSON formats.

---

## 📂 Project Structure

rasa-project/
│
├── actions/
│   └── actions.py
│
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   ├── sales.csv
│   ├── employees.xlsx
│   ├── complaints.json
│
├── config.yml
├── domain.yml
├── endpoints.yml

---

## ⚙️ How to Run Project

pip install rasa pandas openpyxl  
rasa train  
rasa run actions  
rasa shell  

---

## 📌 TASKS (30–51) EXPLANATION

### 🧠 30. Custom Action File
Creates backend logic for chatbot responses using Python.

### 📊 31. Pandas Import
Used for data analysis and manipulation.

### 📈 32. Sales DataFrame
Creates sample dataset for testing.

### 💰 33. Total Sales
Calculates total revenue from sales data.

### 📉 34. Average Sales
Finds average sales value.

### 🏆 35. Highest Sales
Identifies best performing product.

### 📉 36. Lowest Sales
Identifies weakest product.

### 💹 37. Profit Percentage
Calculates profit efficiency.

### 💬 38. Return Chatbot Message
Displays output to user.

### 📁 39. CSV File Handling
Loads sales dataset from file.

### 📊 40. Excel File Handling
Loads employee dataset from Excel.

### 🧾 41. JSON File Handling
Loads complaint dataset.

### 🏅 42. Top Selling Product
Finds highest revenue product.

### 📉 43. Least Selling Product
Finds lowest revenue product.

### 👨‍💼 44. Total Employees
Counts total employees.

### 🌟 45. Best Employee
Finds top performer.

### ⚠️ 46. Most Common Complaint
Finds repeated complaints.

### 🚫 47. Missing File Handling
Prevents program crash if file missing.

### ❌ 48. Invalid Excel Handling
Handles wrong file format errors.

### 🔁 49. Try-Except Blocks
Prevents runtime crashes.

### 🐞 50. Debug Messages
Used for debugging in terminal.

### 📝 51. Logging System
Stores chatbot activity logs for monitoring.

---

## 🧠 Technologies Used

- Python
- Rasa Open Source
- Pandas
- CSV / Excel / JSON
- NLP (DIETClassifier)

---

## 🎯 Features

✔ AI Chatbot  
✔ Sales Analytics  
✔ Employee Performance Tracking  
✔ Complaint Analysis  
✔ File Integration System  
✔ Error Handling System  
✔ Logging System  

---

## 💡 Example Output

User: total sales  
Bot: 📊 Total Sales: 150000  

---


Weekly Task (30–51) Rasa Chatbot Project
