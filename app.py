import streamlit as st
import psutil
import time

def get_system_stats():
    stats = {}

    # Accurate CPU usage per core
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    stats['cpu'] = [{'core': i + 1, 'usage': min(usage, 100.0)} for i, usage in enumerate(cpu_percent)]

    # Memory stats
    memory = psutil.virtual_memory()
    stats['memory'] = {
        'percent': memory.percent,
        'total': memory.total / (1024 ** 3),
        'available': memory.available / (1024 ** 3),
        'used': memory.used / (1024 ** 3)
    }

    # Top 15 processes
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            name = proc.info['name'].lower()
            pid = proc.info['pid']

            if pid == 0 or name in ['system idle process', 'idle', 'system']:
                continue

            cpu = min(proc.info['cpu_percent'], 100.0)
            mem = min(proc.info['memory_percent'], 100.0)
            processes.append({
                'PID': pid,
                'Name': proc.info['name'][:25],
                'CPU %': cpu,
                'Memory %': mem
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    stats['processes'] = sorted(processes, key=lambda p: p['CPU %'], reverse=True)[:15]
    return stats

def display_system_stats():
    st.set_page_config(page_title="System Monitor", layout="wide")
    st.title("🖥️ Real-Time System Monitor")

    placeholder = st.empty()

    while True:
        with placeholder.container():
            stats = get_system_stats()

            # CPU Usage
            st.subheader("🖥️ CPU Usage")
            cols = st.columns(4)
            for i, core in enumerate(stats['cpu']):
                with cols[i % 4]:
                    st.write(f"Core {core['core']}: {core['usage']:.2f}%")
                    st.progress(core['usage'] / 100)

            # Memory Usage
            st.subheader("🗄️ Memory Usage")
            st.write(f"Usage: {stats['memory']['percent']:.2f}%")
            st.write(f"Total: {stats['memory']['total']:.2f} GB")
            st.write(f"Available: {stats['memory']['available']:.2f} GB")
            st.write(f"Used: {stats['memory']['used']:.2f} GB")

            # Top Processes
            st.subheader("📋 Top 15 Processes by CPU Usage")
            for proc in stats['processes']:
                cols = st.columns([2, 4, 2, 2, 2])
                cols[0].write(f"PID: {proc['PID']}")
                cols[1].write(f"Name: {proc['Name']}")
                cols[2].write(f"CPU: {proc['CPU %']:.2f}%")
                cols[3].write(f"Memory: {proc['Memory %']:.2f}%")
                if cols[4].button("❌ Kill", key=f"kill_{proc['PID']}"):
                    try:
                        p = psutil.Process(proc['PID'])
                        p.terminate()
                        st.success(f"Killed PID {proc['PID']} ({proc['Name']})")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Could not kill PID {proc['PID']}: {e}")

        time.sleep(10)  # Refresh every 10 seconds
        st.rerun() 
if __name__ == "__main__":
    try:
        display_system_stats()
    except KeyboardInterrupt:
        st.write("System Monitor Stopped.")
