# test/__init__.py

# Allow tests to import from src package
import sys
import os

# Add project root to PYTHONPATH so pytest/unittest can find src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
