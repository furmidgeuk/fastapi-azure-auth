# FastAPI + Azure AD Authentication Example

This repository demonstrates how to secure a **FastAPI** backend with **Azure Active Directory** using OAuth2, with the help of [`fastapi-azure-auth`](https://github.com/janmichael92/fastapi-azure-auth).

## 🚀 Features

- FastAPI backend
- OAuth2 authentication via Azure AD (Single Tenant)
- Secured endpoints using Azure-issued access tokens
- Swagger UI OAuth2 login support
- CORS enabled for frontend integration
- Example student data endpoint
- Uses `.env` for configuration (client IDs, tenant ID, etc.)

## 📁 Project Structure

```
.
├── .env                # Not committed - contains secrets
├── auth.py             # Azure AD token validation setup
├── main.py             # FastAPI app entry point
└── students/
    ├── students.py     # API route for /api/students
    └── students.json   # Mock student data
```

## 🧰 Prerequisites

1. Azure AD Tenant
2. Two App Registrations:
   - Frontend: `devopswithdave-fe`
   - Backend: `devopswithdave-be`
3. Expose an API scope in the backend app: `access_as_user`

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/furmidgeuk/fastapi-azure-auth.git
cd fastapi-azure-auth
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn fastapi-azure-auth python-dotenv
```

### 4. Create a `.env` File

Create a `.env` file in the project root:

```env
AZURE_CLIENT_ID=your-backend-client-id
AZURE_TENANT_ID=your-tenant-id
AZURE_API_SCOPE=api://devopswithdave-be/access_as_user
FRONTEND_CLIENT_ID=your-frontend-client-id
```

Add `.env` to your `.gitignore`.

---

## ▶ Run the App

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

Click **"Authorize"** to login with Azure AD and get a token for testing.

---

## 🗂 Full Tutorial

📖 [Read the blog post for full setup instructions](https://devopswithdave.com/azure/spa/oauth/post-az-easy-auth-p2/)

---

## 📌 Notes

- Ensure the frontend app registration allows the redirect URI:  
  `http://localhost:8000/oauth2-redirect`
- This is a local development example. For production, ensure secure HTTPS and client secret handling.

---

## 📄 License

MIT
