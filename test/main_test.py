import pytest
from app.main import upload_3d_object


@pytest.mark.asyncio
async def test_file_uploading():
    response = await upload_3d_object(open("C:/Users/ct67ca/Documents/dev/tcc/API/26-08/serve-unity-app-api/files/fbx_objects/test.fbx", "rb"))
    print(response)
    assert response == "ok"