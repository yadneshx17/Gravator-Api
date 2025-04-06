# Gravatar API

This is a FastAPI-based wrapper for the **gmailtogravatar.py** OSINT tool. It provides Gravatar profile information via a RESTful API.

## Installation

### Prerequisites
- Python 3.9+
- FastAPI
- Uvicorn
- Docker (optional, for containerized deployment)

### Clone the Repository
```bash
git clone https://github.com/yadneshx17/gravatar-api.git
cd gravatar-api
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### API Key Setup
- Create a `.env` file in the project root:
  ```
  API_KEY=your-secret-api-key
  ```
- If `.env` is present, it will use this key. Otherwise, it defaults to `default-api-key`.

## Running the API

### Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Using Docker
#### Build and Run the Container
```bash
docker build -t gravatar-api .
docker run -d -p 8000:8000 --env-file .env gravatar-api
```

## API Usage

### Endpoint
```
GET /gravatar/{email}
```

### Headers
```
X-API-Key: your-secret-api-key
```

### Example Request
```bash
curl -H "X-API-Key: your-secret-api-key" http://localhost:8000/gravatar/example@example.com
```

### Example Response
```json
{
  "display_name": "Knight Hawk",
  "preferred_username": "meerkatgracefully399444c69f",
  "profile_url": "https://gravatar.com/meerkatgracefully399444c69f",
  "thumbnail_url": "https://0.gravatar.com/avatar/56f388c3496feddf6a1a87ad23329913",
  "about_me": "N/A",
  "location": "N/A"
}
```
