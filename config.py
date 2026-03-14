import os

# You need to fill in your actual API_ID or set it as an environment variable
API_ID = int(os.environ.get("API_ID", "34002235"))  # Replace 123456 with your actual ID or set via env

API_HASH = os.environ.get("API_HASH", "a20787c224809296fa50dcc3e9824b3f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8622331139:AAFsqZPlPvOf8InB_zaN-bhvcgcz6ncTK88")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

# Make sure OWNER is provided in environment or hardcode it here
OWNER = int(os.environ.get("OWNER", "8429501123"))  # Replace with your Telegram ID or set via env

# Replace with actual log chat ID or default value
LOG = int(os.environ.get("LOG", "-1003642874957"))  # Replace with your log group/channel ID

# UPDATE_GRP = int(os.environ.get("UPDATE_GRP", "-100xxxxxxxxxx"))  # Optional: uncomment if used
# auth_chats = []  # Optional: add if required

try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "8429501123").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Make sure OWNER is included in ADMINS
if OWNER not in ADMINS:
    ADMINS.append(OWNER)
