import allure

@allure.feature("帖子模块")
class TestPost:


    @allure.story("查询帖子")
    @allure.title("获取帖子列表")
    def test_get_posts(self, post_api):
        r = post_api.get_posts()
        assert r.status_code == 200
        assert len(r.json()) == 100

    @allure.story("创建帖子")
    @allure.title("创建帖子成功")
    def test_create_post(self, post_api):
        payload = {"title":"foo", "body": "bar", "userId":1}
        r = post_api.create_post(payload)
        assert r.status_code == 201
        assert r.json()["title"] == "foo"

    @allure.story("删除帖子")
    @allure.title("删除帖子成功")
    def test_delete_post(self, post_api):
        r = post_api.delete_post(1)
        assert r.status_code == 200
