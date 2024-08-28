from app.ui.layout.layout import AppLayout
from app.ui.route.router import AppRoutes

if __name__ == "__main__":
    app_layout = AppLayout(route_handler=None)

    app_routes = AppRoutes(app_layout)

    app_layout.route_handler = app_routes.select_frame_by_name

    app_routes.select_frame_by_name("home")

    app_layout.mainloop()
