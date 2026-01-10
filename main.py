import subprocess
import os
import sys

def main():
    base = sys._MEIPASS if hasattr(sys, "_MEIPASS") else os.getcwd()
    app_path = os.path.join(base, "app.py")

    # Absolute path to streamlit inside venv
    streamlit_exe = os.path.join(
        os.getcwd(),
        "venv",
        "Scripts",
        "streamlit.exe"
    )

    if not os.path.exists(streamlit_exe):
        raise RuntimeError("streamlit.exe not found in venv")

    subprocess.Popen(
        [
            streamlit_exe,
            "run",
            app_path,
            "--server.address",
            "127.0.0.1",
            "--server.port",
            "8501",
        ],
        cwd=os.getcwd()
    )

if __name__ == "__main__":
    main()
