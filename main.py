from fastapi import FastAPI, UploadFile

from services.azure_db import AzureDatabase
from services.database_manager import DatabaseManager
from utils import Utils

app = FastAPI()
FBX_OBJECT_FOLDER = "files/fbx_objects"
TUTORIAL_VIDEO_FOLDER = "files/tutorial_videos"

@app.get("/")
def index():
    return {
        "main_route": "/acessfile/"
    }

@app.post("/uploadfile/")
async def upload_3d_object_and_tutorial_video(object_3d: UploadFile, tutorial_video: UploadFile):
    try:
        db = DatabaseManager(AzureDatabase)
    except Exception as e:
        print(e)
        raise Exception("Could not connect to the database.")

    try:
        with open(f"{FBX_OBJECT_FOLDER}\{object_3d.filename}", "wb") as folder:
            content = await object_3d.read()
            # necessita de testes do que acontece se ja houver um arquivo / etc
            folder.write(content)

        with open(f"{TUTORIAL_VIDEO_FOLDER}\{tutorial_video.filename}", "wb") as folder:
            content = await tutorial_video.read()
            folder.write(content)

        file_path = f"{FBX_OBJECT_FOLDER}\{object_3d.filename}"
        video_path = f"{TUTORIAL_VIDEO_FOLDER}\{tutorial_video.filename}"

    except Exception as e:
        return "An exception ocurred: "+ str(e)

    video_upload_status = False
    object_upload_status = False

    object_extension = Utils.get_file_extension(str(object_3d.filename))
    object_name = Utils.get_only_file_name(str(object_3d.filename))
    video_extension = Utils.get_file_extension(str(tutorial_video.filename))
    video_new_name = str(object_name+"."+video_extension)

    try:
        upload = db.upload_3d_object(file_path, str(object_3d.filename))
        if upload != "Upload successful":
            object_upload_status = False
        else:
            object_upload_status = True
            Utils.delete_file_locally(file_path)
    except Exception as e:
        print(e)
        raise Exception("Could not upload the file.")

    try:
        # the tutorial video will have the same name as its 3d file for better indexing
        upload = db.upload_video(video_path, video_new_name)
        if upload != "Upload successful":
            video_upload_status = False
        else:
            video_upload_status = True
            Utils.delete_file_locally(video_path)
    except Exception as e:
        print(e)
        raise Exception("Could not upload the video.")

    if video_upload_status == True & object_upload_status == True:
        return {
                    "object_3d": object_3d.filename,
                    "video": tutorial_video.filename,
                    "object_3d_upload": video_upload_status,
                    "video_upload": video_upload_status,
                    "sucess": True
                }

    return {
        "object_3d": object_3d.filename,
        "video": tutorial_video.filename,
        "object_3d_upload": video_upload_status,
        "video_upload": video_upload_status,
        "sucess": False
    }
