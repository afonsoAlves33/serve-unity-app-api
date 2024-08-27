import time

from services.azure_blob_storage import AzureStorage
from services.storage_manager import StorageManager

db = StorageManager(AzureStorage)
#
# db.de("dst", "sdt")
az = AzureStorage()
print(az.delete_video("3.mp4"))
print(az.delete_3d_object("3.fbx"))
print("time waiting")
time.sleep(5)
print("time done")
print(az.delete_video("3.mp4"))
print(az.delete_3d_object("3.fbx"))