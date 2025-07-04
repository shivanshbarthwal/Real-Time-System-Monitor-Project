# 🖥️ Real-Time System Monitor

A real-time system monitoring web app built with **Streamlit** and **psutil**. This tool lets you monitor CPU and memory usage, and view the top 15 processes sorted by CPU usage. You can also kill any process directly from the interface.

## 🔍 Features

- 📊 **CPU Monitoring**: Live usage per core with progress bars.
- 🧠 **Memory Monitoring**: Total, available, used, and percentage usage.
- 📋 **Top Processes**: View top 15 processes by CPU usage.
- ❌ **Kill Process Button**: Terminate unnecessary processes from the UI.
- 🔄 **Auto Refresh**: Updates every 10 seconds.

## 🛠️ Technology Stack

- **Python 3**
- **Streamlit** – For building interactive web UI
- **psutil** – For accessing system-level information

## 📦 Requirements

Install the required Python packages:

```bash
pip install streamlit psutil
```

## 🚀 How to Run

Run the Streamlit app using:

```bash
streamlit run app.py
```

> Make sure the file is named `app.py` or change the command accordingly.

## 📁 File Structure

```
real-time-system-monitor/
├── app.py            # Main Streamlit application
├── README.md         # Documentation file
```

## 🛡️ Notes

- Run as administrator/root to kill system-level processes.
- Tested on Windows. Should work on Linux and macOS with minor tweaks.
- Some processes may not be accessible due to OS-level permissions.

---

Made by using [Streamlit](https://streamlit.io/) and [psutil](https://pypi.org/project/psutil/)
