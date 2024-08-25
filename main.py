# import customtkinter as ctk
# import app.config.settings as settings
# import os
# import sys
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time


# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("アプリ")
#         self.geometry("1200x800")

#         # リサイズしたときに一緒に拡大したい行をweight 1に設定
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         image_path = settings.IMAGE_PATH


# ## 以下のコードは、ファイルの変更を検知してアプリケーションを再起動するためのコード
# class RestartHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith(".py"):
#             print(f"変更検知: {event.src_path}. アプリケーションを再起動します。")
#             os.execv(sys.executable, ["python"] + sys.argv)


# def start_observer(path):
#     event_handler = RestartHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()


# if __name__ == "__main__":
#     # 引数で指定したディレクトリー配下のファイルの変更を検知してアプリケーションを再起動する
#     start_observer("app")
#     app = App()
#     app.mainloop()

from app.ui.layout import AppLayout
from app.ui.router import AppRoutes

if __name__ == "__main__":
    # Initialize Layout with Route Handler
    app_layout = AppLayout(route_handler=None)

    # Initialize Routes with Layout
    app_routes = AppRoutes(app_layout)

    # Link the route handler in layout to the routes
    app_layout.route_handler = app_routes.select_frame_by_name

    # Select default frame
    app_routes.select_frame_by_name("home")

    # Run the app
    app_layout.mainloop()
