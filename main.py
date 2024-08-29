from app.ui.layout.layout import AppLayout
from app.ui.route.router import AppRoutes


def main():
    """
    依存性注入(DI)を行い、router部分にAppLayoutのインスタンスを渡して
    router部分でAppLayoutのインスタンスを操作するように

    テストがしやすくなるし、layout部分が肥大化してもrouter部分に分離できる
    """
    app_layout = AppLayout(route_handler=None)

    app_routes = AppRoutes(app_layout)

    app_layout.route_handler = app_routes.select_frame_by_name

    app_routes.select_frame_by_name("home")

    app_layout.mainloop()


if __name__ == "__main__":

    main()
