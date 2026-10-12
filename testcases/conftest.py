#fixture：注入API对象
import pytest
from api.user_api import UserApi
from api.post_api import PostApi

@pytest.fixture(scope = "session")
def user_api():
    return UserApi()

@pytest.fixture(scope = "session")
def post_api():
    return PostApi()