import os
import pytest
from app.utils import Utils

dir = os.getcwd()

def test_get_file_extension():
    assert Utils.get_file_extension("anythingThatDoesNotExist.txt") == "txt"
    
def test_get_file_name():
    assert Utils.get_file_name("anythingThatDoesNotExist.txt") == "anythingThatDoesNotExist"

def test_delete_file_locally():
    with open(str(dir)+"/files/anything.txt", "w") as file:
        file.write("anything just to test")
    assert Utils.delete_file_locally(str(dir)+"/files/anything.txt") == "File deleted"
