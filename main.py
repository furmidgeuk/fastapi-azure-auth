import os
from dotenv import load_dotenv
from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from students import students
from auth import azure_scheme

load_dotenv()

app = FastAPI(
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': os.getenv("FRONTEND_CLIENT_ID"),
        'scopes': os.getenv("AZURE_API_SCOPE")
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(students.router, dependencies=[Security(azure_scheme)])