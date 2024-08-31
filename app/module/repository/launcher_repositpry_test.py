import unittest
import json

from app.config.settings import BASE_DIR

from app.module.repository.launcher_repositpry import LauncherRepository


class TestLauncherRepository(unittest.TestCase):

    def test_save_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        with open(launcher_repository.save_path, "r") as f:
            data = json.load(f)
            self.assertEqual(data["test_key"], "home\\doc\\test_path.exe")

    def test_load_launch_path(self):
        launcher_repository = LauncherRepository()
        launcher_repository.save_launch_path(
            key="test_key", launch_app_path="home\\doc\\test_path.exe"
        )
        data = launcher_repository.load_launch_path(key="test_key")
        self.assertEqual(data, "home\\doc\\test_path.exe")
