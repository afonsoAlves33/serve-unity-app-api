from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

from database_interface import Database

load_dotenv()

class AzureDatabase(Database):
    def __init__(self) -> None:
        super().__init__()

    storage_account_key = os.environ['storage_account_key']
    storage_account_name = os.environ['storage_account_name']
    connection_string = os.environ['connection_string']
    objects3d_container_name = os.environ['OBJECTS3D_CONTAINER']
    videos_container_name = os.environ['VIDEOS_CONTAINER']
    object3d_filepath = "C:/Users/ct67ca/Documents/dev/tcc/API/01-08/serve-unity-app-api/files/fbx_objects/3.fbx"
    video_filepath = "C:\\Users\\ct67ca\\Documents\\dev\\tcc\API\\01-08\\serve-unity-app-api\\files\\tutorial_videos\\WIN_20240802_14_13_24_Pro.mp4"

    def upload_3d_object(self, file_path, file_name):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        blob_client = blob_service_client.get_blob_client(container=self.objects3d_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(e)

        print("Sucesso no upload do objeto 3d!")

    def upload_video(self, file_path, file_name):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        blob_client = blob_service_client.get_blob_client(container=self.videos_container_name, blob=file_name)
        try: 
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(e)

        print("Sucesso no upload do video!")
        

AzureDatabase.upload_3d_object(AzureDatabase.object3d_filepath, "3.fbx")
AzureDatabase.upload_video(AzureDatabase.video_filepath, "3.mp4")