from pymongo import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
import os
from dotenv import load_dotenv


#loading environement variables

load_dotenv()

# Retrieve the password from environment variables
password = os.getenv("MONGO_PASSWORD")

# Check if password is None or empty
if not password:
    raise ValueError("PASSWORD environment variable is not set")

# Encode the password for inclusion in the URI
encoded_password = urllib.parse.quote_plus(password)

# Construct the MongoDB URI
uri = f"mongodb+srv://academie_franco:{encoded_password}@atlascluster.gwjj1uh.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

try:
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("An error occurred while connecting to MongoDB:")
    print(e)
