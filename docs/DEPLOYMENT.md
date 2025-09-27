# Deployment Guide

## Production Deployment

### Backend Deployment

#### Using Docker (Recommended)

1. Create a Dockerfile in the backend directory:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 5000
   
   CMD ["python", "run.py"]
   ```

2. Build and run:
   ```bash
   docker build -t cure-connect-backend .
   docker run -p 5000:5000 cure-connect-backend
   ```

#### Using Traditional Hosting

1. Set up a virtual environment on your server
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Use a WSGI server like Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 src.api.main:app
   ```

### Frontend Deployment

#### Using Vercel (Recommended)

1. Connect your repository to Vercel
2. Set build command: `npm run build`
3. Set output directory: `.next`
4. Deploy automatically on push

#### Using Netlify

1. Build the project: `npm run build`
2. Upload the `out` directory to Netlify
3. Configure redirects for SPA routing

#### Using Traditional Hosting

1. Build the project: `npm run build`
2. Serve the static files using nginx or Apache

## Environment Variables

### Backend
- `FLASK_ENV`: production
- `SECRET_KEY`: Your secret key
- `DATABASE_URL`: Database connection string (if applicable)

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL
- `NEXT_PUBLIC_ENVIRONMENT`: production

## Monitoring and Logging

- Set up application monitoring (e.g., Sentry)
- Configure logging for production
- Set up health checks for both services
