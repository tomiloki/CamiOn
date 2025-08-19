from fastapi import FastAPI

from .settings import settings  # noqa: F401  (se usará en iteraciones siguientes)

app = FastAPI(title="CamiON API", version="0.0.1")


@app.get("/health")
def health():
    """
    Healthcheck simple para CI/monitorización.
    Devuelve estado y metadatos mínimos de la app.
    """
    return {"status": "ok", "app": "CamiON API", "version": app.version}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
