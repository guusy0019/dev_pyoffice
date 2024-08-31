from app.module.repository.launcher_repositpry import LauncherRepository


class LauncherUsecase:

    def save_launch_path(self, *, key: str, launch_app_path: str):
        launcer_repository = LauncherRepository()
        launcer_repository.save_launch_path(key=key, launch_app_path=launch_app_path)

    def get_launch_path(self, *, key: str) -> str:
        launcer_repository = LauncherRepository()
        return launcer_repository.get_launch_path(key=key)

    def get_all_launch_path(self) -> dict[str, str]:
        launcer_repository = LauncherRepository()
        return launcer_repository.get_all_launch_path()

    def delete_launch_path(self, *, key: str) -> None:
        launcer_repository = LauncherRepository()
        launcer_repository.delete_launch_path(key=key)
