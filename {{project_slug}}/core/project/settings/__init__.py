from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env: environ.Env = environ.Env()
env.read_env(Path(BASE_DIR / ".env"))

ENVIRONMENT = env.str("ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    from .production import *
else:
    from .development import *

__all__ = ["env", "BASE_DIR", "ENVIRONMENT"]
