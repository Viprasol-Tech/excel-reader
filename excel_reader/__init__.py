"""
excel-reader - Read Excel files with sheet detection

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ExcelReader, read, process, main

__all__ = ["ExcelReader", "read", "process", "main"]
