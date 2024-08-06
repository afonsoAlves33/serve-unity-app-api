import time

from azure_db_implementation import AzureDatabase
from database_manager import DatabaseManager

db = DatabaseManager(AzureDatabase)
#
# db.de("dst", "sdt")
az = AzureDatabase()
print(az.delete_video("3.mp4"))
print(az.delete_3d_object("3.fbx"))
print("time waiting")
time.sleep(5)
print("time done")
print(az.delete_video("3.mp4"))
print(az.delete_3d_object("3.fbx"))