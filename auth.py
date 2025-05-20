import os
from dotenv import load_dotenv
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer

load_dotenv()
azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=os.getenv("AZURE_CLIENT_ID"),
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    scopes={os.getenv("AZURE_API_SCOPE"): "access_as_user"},
    allow_guest_users=True
)