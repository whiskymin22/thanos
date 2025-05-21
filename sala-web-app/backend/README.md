# Sala Web Application Backend

This README file provides an overview of the backend service for the Sala Web Application, which is built using FastAPI, PostgreSQL, and Docker.

## Project Structure

The backend service is organized into the following directories:

- **app**: Contains the main application code.
  - **api**: Contains the API endpoints.
    - **endpoints**: Contains individual endpoint files.
  - **core**: Contains core configuration and database connection logic.
  - **models**: Contains database models.
  - **schemas**: Contains Pydantic schemas for data validation.
  - **services**: Contains service logic for processing data.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd sala-web-app/backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   Update the database connection settings in `app/core/config.py` to match your PostgreSQL setup.

5. **Run the Application**
   You can run the FastAPI application using:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Docker Setup**
   To build and run the application using Docker, use the following commands:
   ```bash
   docker build -t sala-backend .
   docker run -d -p 8000:8000 sala-backend
   ```

## API Endpoints

- **Upload Excel File**
  - **Endpoint**: `/api/upload`
  - **Method**: `POST`
  - **Description**: Accepts an Excel file upload and processes the data.

## Additional Information

For more details on the frontend service, please refer to the `frontend/README.md` file.

For any issues or contributions, please refer to the main project repository.