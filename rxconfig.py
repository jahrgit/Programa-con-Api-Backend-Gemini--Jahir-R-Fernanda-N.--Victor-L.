import reflex as rx

config = rx.Config(
    app_name="api_programas",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)