#!/usr/bin/env python3
import subprocess
import sys
import os

if __name__ == "__main__":
    print("Starting A-BOT frontend...")
    print("Make sure the backend server is running first!")
    print("Frontend will be available at: http://localhost:8501")
    print("Press Ctrl+C to stop the frontend")
    
    # Change to the src/frontend directory
    frontend_dir = os.path.join(os.path.dirname(__file__), 'src', 'frontend')
    os.chdir(frontend_dir)
    
    # Start streamlit
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "app.py",
        "--server.port", "8501",
        "--server.address", "0.0.0.0"
    ]) 