# type: ignore
"""Primary API."""
import orjson
import psycopg2
from .extra import psycopg2_register_uuid_stub  # noqa: F401, I201, I100

from fastapi import (
    Depends,
    FastAPI,
    Request,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from .routers.alerts import router as alert_router
from .routers.charts import router as chart_router
from .routers.etl import router as etl_router
from .routers.networks import router as network_router
from .routers.nlp import router as nlp_router
from .routers.posts import router as post_router
from .routers.products import router as product_router
from .routers.projects import router as project_router
from .routers.sources import router as source_router
from .routers.users import router as user_router
from .settings import ALLOW_ORIGINS, SERVICE_NAME
from .utils import verify_developer_token

# Use ORJSON decoder for parsing responses from postgresql
psycopg2.extras.register_default_jsonb(loads=orjson.loads, globally=True)
# Global service logger
s_lg = logger.create_service_lg(SERVICE_NAME)

app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    alert_router.router,
    prefix="/alert",
    tags=["alert"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    chart_router.router,
    prefix="/dashboard",
    tags=["dashboard"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    etl_router.router,
    prefix="/etl",
    tags=["etl"],
)
app.include_router(
    network_router.router,
    prefix="/network",
    tags=["network"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    nlp_router.router,
    prefix="/nlp",
    tags=["nlp"],
    dependencies=[Depends(verify_developer_token)],
)
app.include_router(
    post_router.router,
    prefix="/post",
    tags=["post"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    product_router.router,
    prefix="/product",
    tags=["product"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    project_router.router,
    prefix="/project",
    tags=["project"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    source_router.router,
    prefix="/source",
    tags=["source"],
    dependencies=[Depends(get_db)],
)
app.include_router(
    user_router.router,
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_db)],
)


@app.middleware("http")
async def run_middleware(request: Request, call_next):
    """Middleware that runs before a request is processed and a response is returned.

    The exit logic of dependencies with yield runs after the middleware. Background
    tasks run after the middleware.
    """
    response = await call_next(request)
    # Delete the context logger if it exists
    logger.delete()
    return response


@app.get("/")
def index():
    """Index route."""
    return "Hello from Yogi API."
