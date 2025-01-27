import uvicorn

import config


def main():
    settings = config.get_settings()
    uvicorn.run(
        app="fastapi_server:app",
        host=settings.listen_host,
        port=int(settings.listen_port),
        reload=settings.env != config.AppEnvironment.PROD,
        workers=1,
    )


if __name__ == "__main__":
    main()
