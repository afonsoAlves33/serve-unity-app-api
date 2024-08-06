from fastapi import FastAPI, UploadFile

from services.azure_db import AzureDatabase
from services.database_manager import DatabaseManager

app = FastAPI()
FBX_OBJECT_FOLDER = "files/fbx_objects"
TUTORIAL_VIDEO_FOLDER = "files/tutorial_videos"


@app.post("/uploadfile/")
async def receive_3d_object_and_its_tutorial_video(object_3d: UploadFile, tutorial_video: UploadFile):
    try:
        # file_path = ""
        # video_path = ""
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

    db = DatabaseManager(AzureDatabase)
    print(db.upload_3d_object(file_path, "new file.fbx"))
    print(db.upload_video(video_path, "new file.mp4"))

    return {
                "video": tutorial_video.filename,
                "object_3d": object_3d.filename,
                "sucess": True
            }
