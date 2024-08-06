from azure_db_implementation import AzureDatabase
from database import DatabaseManagement

db = DatabaseManagement(AzureDatabase)

db.upload_3d_object("dst", "sdt")