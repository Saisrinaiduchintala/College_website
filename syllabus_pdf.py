from pymongo import MongoClient
from pymongo.server_api import ServerApi
import gridfs

import os
from dotenv import load_dotenv

load_dotenv()


# MongoDB connection
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, server_api=ServerApi("1"))

db = client["College"]

# GridFS storage
fs = gridfs.GridFS(db)


# PDF file
pdf_path = "CSE-R24 (1)(1).pdf"


# Store PDF in MongoDB
with open(pdf_path, "rb") as pdf_file:

    file_id = fs.put(
        pdf_file,
        filename="CSE-R24 (1)(1).pdf",
        content_type="application/pdf"
    )


print("Syllabus PDF uploaded successfully!")
print("File ID:", file_id)