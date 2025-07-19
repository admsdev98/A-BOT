import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from views.cookies_ui import show_cookies_info

show_cookies_info() 