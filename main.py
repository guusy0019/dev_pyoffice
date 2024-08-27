from app.ui.layout.layout import AppLayout
from app.ui.route.router import AppRoutes

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
