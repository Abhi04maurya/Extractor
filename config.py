# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "3670291"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "1f55b2e9d972c3a5ac3f008c51ed7a4a")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7545498255:AAE6-l7q9j76rC1qpT7_3G_QN_FstKtMMM4")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "659925627"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-100"))

