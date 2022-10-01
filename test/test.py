import os
import sys 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tps import topread


if __name__ == "__main__":
    test = topread("C:\\Redcat\\POS\\tbl_dbconn.tps", "@dbc:")
    print()