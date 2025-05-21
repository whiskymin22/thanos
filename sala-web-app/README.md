# sala-web-app

This project is a web application that allows users to upload Excel files for processing. It is built using FastAPI for the backend, React for the frontend, and Streamlit for additional data visualization. The application uses PostgreSQL as the database and is containerized using Docker.

## Project Structure

```
sala-web-app
├── backend
│   ├── app
│   │   ├── main.py                # Entry point for the FastAPI application
│   │   ├── api
│   │   │   ├── endpoints
│   │   │   │   └── upload.py      # Endpoint for uploading Excel files
│   │   │   └── __init__.py
│   │   ├── core
│   │   │   ├── config.py          # Configuration settings
│   │   │   └── database.py        # Database connection handling
│   │   ├── models
│   │   │   └── __init__.py
│   │   ├── schemas
│   │   │   └── upload.py          # Pydantic schemas for file validation
│   │   └── services
│   │       └── process_excel.py   # Logic for processing uploaded Excel files
│   ├── Dockerfile                  # Dockerfile for backend service
│   ├── requirements.txt            # Python dependencies for backend
│   └── README.md                   # Documentation for backend service
├── frontend
│   ├── public
│   │   └── index.html              # Main HTML file for React application
│   ├── src
│   │   ├── components
│   │   │   └── FileUpload.js       # React component for file uploads
│   │   ├── pages
│   │   │   └── HomePage.js         # Main page of the React application
│   │   ├── App.js                  # Main component of the React application
│   │   └── index.js                # Entry point for the React application
│   ├── package.json                # npm configuration for frontend
│   ├── Dockerfile                  # Dockerfile for frontend service
│   └── README.md                   # Documentation for frontend service
├── streamlit
│   ├── app.py                      # Streamlit application code
│   └── requirements.txt            # Python dependencies for Streamlit application
├── docker-compose.yml              # Docker orchestration file
└── README.md                       # Overall project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd sala-web-app
   ```

2. **Backend Setup:**
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn app.main:app --reload
     ```

3. **Frontend Setup:**
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

4. **Streamlit Setup:**
   - Navigate to the `streamlit` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the Streamlit application:
     ```
     streamlit run app.py
     ```

5. **Docker Setup:**
   - Ensure Docker is installed and running.
   - Build and run the application using Docker Compose:
     ```
     docker-compose up --build
     ```

## Usage

- Users can upload Excel files through the frontend interface.
- The backend processes the uploaded files and stores the relevant data in the PostgreSQL database.
- The Streamlit application provides additional data visualization and analysis features.

## License

This project is licensed under the MIT License.