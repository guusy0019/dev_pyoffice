import unittest

from app.module.service.launcher_service import LauncherService


class TestLauncherService(unittest.TestCase):

    def test_save_launch_path(self):
        launcher_service = LauncherService()
        launcher_service.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        data = launcher_service.get_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.exe")

    def test_get_launch_path(self):
        launcher_service = LauncherService()
        launcher_service.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        data = launcher_service.get_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.exe")

    def test_get_all_launch_path(self):
        launcher_service = LauncherService()
        launcher_service.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        data = launcher_service.get_all_launch_path()
        self.assertEqual(data["test_key"], "home\\doc\\test_path.exe")

    def test_delete_launch_path(self):
        launcher_service = LauncherService()
        launcher_service.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        launcher_service.delete_launch_path(key="test_key")
        data = launcher_service.get_launch_path(key="test_key")
        self.assertEqual(data, "")
