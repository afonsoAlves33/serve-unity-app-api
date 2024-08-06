from azure_db_implementation import AzureDatabase
from database_manager import DatabaseManager

db = DatabaseManager(AzureDatabase)

db.upload_3d_object("dst", "sdt")