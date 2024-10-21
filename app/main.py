from fastapi import FastAPI, UploadFile, status, Response, HTTPException
from app.utils import Utils
from services.azure_blob_storage.azure_storage import AzureStorage
from services.azure_blob_storage.storage_manager import StorageManager


app = FastAPI()
FBX_OBJECT_FOLDER = "files/fbx_objects"
TUTORIAL_VIDEO_FOLDER = "files/tutorial_videos"

@app.get("/")
def index():
    return {
        "routes": ["/upload_file/", "/upload_object/", "/upload_video/"]
    }

@app.post("/upload_file/", status_code=201)
async def upload_3d_object_and_tutorial_video(object_3d: UploadFile, tutorial_video: UploadFile, response: Response):
    try:
        sm = StorageManager(AzureStorage)
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
    object_name = Utils.get_file_name(str(object_3d.filename))
    video_extension = Utils.get_file_extension(str(tutorial_video.filename))
    video_new_name = str(object_name+"."+video_extension)

    try:
        upload = sm.upload_3d_object(file_path, str(object_3d.filename))
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
        upload = sm.upload_video(video_path, video_new_name)
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
                    "success": True
                }

    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return {
        "object_3d": object_3d.filename,
        "video": tutorial_video.filename,
        "object_3d_upload": video_upload_status,
        "video_upload": video_upload_status,
        "success": False
    }

@app.post("/upload_object/", status_code=201)
async def upload_3d_object(object_3d: UploadFile, response: Response):

    object_upload_status = False
    object_extension = Utils.get_file_extension(str(object_3d.filename))
    object_name = Utils.get_file_name(str(object_3d.filename))

    if str(object_extension) != "fbx":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='You should upload ".fbx" files')

    try:
        sm = StorageManager(AzureStorage)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="We had a trouble connecting to the database")

    try:
        with open(f"{FBX_OBJECT_FOLDER}\{object_3d.filename}", "wb") as file_path:
            content = await object_3d.read()
            # necessita de testes do que acontece se ja houver um arquivo / etc
            file_path.write(content)

        file_path = f"{FBX_OBJECT_FOLDER}\{object_3d.filename}" # testar enfiar essa variavel no with open

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error ocurred")



    # Uploads the file to Azure Storage
    try:
        upload = sm.upload_3d_object(file_path, str(object_3d.filename))
        if upload != "Upload successful":
            object_upload_status = False
        else:
            object_upload_status = True
            Utils.delete_file_locally(file_path)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error ocurred, could'nt upload your file")


    if object_upload_status == True:
        return {
                    "object_3d": object_3d.filename,
                    "object_3d_upload": object_upload_status,
                    "success": True
                }
    else: 
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "object_3d": object_3d.filename,
            "object_3d_upload": object_upload_status,
            "success": False
        }

@app.post("/upload_video/", status_code=201)
async def upload_video(video: UploadFile, response: Response):

    object_upload_status = False
    object_extension = Utils.get_file_extension(str(video.filename))
    object_name = Utils.get_file_name(str(video.filename))

    if str(object_extension) == "fbx":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You should upload videos")

    try:
        sm = StorageManager(AzureStorage)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="We had a trouble connecting to the database")

    try:
        with open(f"{TUTORIAL_VIDEO_FOLDER}\{video.filename}", "wb") as file_path:
            content = await video.read()
            # necessita de testes do que acontece se ja houver um arquivo / etc
            file_path.write(content)

        file_path = f"{TUTORIAL_VIDEO_FOLDER}\{video.filename}" # testar enfiar essa variavel no with open

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error ocurred")



    # Uploads the file to Azure Storage
    try:
        upload = sm.upload_video(file_path, str(video.filename))
        if upload != "Upload successful":
            object_upload_status = False
        else:
            object_upload_status = True
            Utils.delete_file_locally(file_path)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error ocurred, could'nt upload your file")


    if object_upload_status == True:
        return {
                    "video": video.filename,
                    "video_upload": object_upload_status,
                    "success": True
                }
    
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return {
        "video": video.filename,
        "video_upload": object_upload_status,
        "success": Falseerror handling
    }
