from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

from database_interface import Database

load_dotenv()


class AzureDatabase(Database):

    def __init__(self):
        self.storage_account_key = os.getenv('storage_account_key')
        self.storage_account_name = os.getenv('storage_account_name')
        self.connection_string = os.getenv('connection_string')
        self.objects3d_container_name = os.getenv('OBJECTS3D_CONTAINER')
        self.videos_container_name = os.getenv('VIDEOS_CONTAINER')
        self.object3d_filepath = "C:\\Users\\ct67ca\\Documents\\dev\\tcc\\API\\01-08\\serve-unity-app-api\\files\\fbx_objects\\3.fbx"
        self.video_filepath = "C:\\Users\\ct67ca\\Documents\\dev\\tcc\\API\\01-08\\serve-unity-app-api\\files\\tutorial_videos\\3.mp4"

    def upload_3d_object(self, file_path, file_name):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        blob_client = blob_service_client.get_blob_client(container=self.objects3d_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(f"Erro ao fazer upload do objeto 3D: {e}")
        else:
            print("Sucesso no upload do objeto 3D!")

    def upload_video(self, file_path, file_name):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        blob_client = blob_service_client.get_blob_client(container=self.videos_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(f"Erro ao fazer upload do vídeo: {e}")
        else:
            print("Sucesso no upload do vídeo!")


if __name__ == "__main__":
    azure_db = AzureDatabase()

    azure_db.upload_3d_object(azure_db.object3d_filepath, "3.fbx")
    azure_db.upload_video(azure_db.video_filepath, "3.mp4")