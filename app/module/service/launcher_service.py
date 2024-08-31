from app.module.usecase.launcher_usecase import LauncherUsecase


class LauncherService:

    def save_launch_path(self, *, key: str, launch_app_path: str) -> None:
        launcher_usecase = LauncherUsecase()
        launcher_usecase.save_launch_path(key=key, launch_app_path=launch_app_path)

    def get_launch_path(self, *, key: str) -> str:
        launcher_usecase = LauncherUsecase()
        return launcher_usecase.get_launch_path(key=key)

    def get_all_launch_path(self) -> dict[str, str]:
        launcher_usecase = LauncherUsecase()
        return launcher_usecase.get_all_launch_path()

    def delete_launch_path(self, *, key: str) -> None:
        launcher_usecase = LauncherUsecase()
        launcher_usecase.delete_launch_path(key=key)
