# Cure-Connect Backend

Flask-based REST API server for the Cure-Connect clinical trial matching platform.

## Quick Start

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment:
   ```bash
   cp .env.example .env
   ```

4. Run the server:
   ```bash
   python run.py
   ```

## Project Structure

```
backend/
├── src/
│   ├── api/           # API routes and endpoints
│   ├── models/        # Data models
│   ├── services/      # Business logic
│   └── utils/         # Utility functions
├── data/              # Data files and preprocessing
├── config/            # Configuration files
├── tests/             # Test files
├── requirements.txt   # Python dependencies
├── setup.py          # Package configuration
└── run.py            # Application entry point
```

## API Endpoints

See [API Documentation](../docs/API.md) for detailed endpoint information.

## Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Write docstrings for functions and classes

### Testing
```bash
pytest tests/
```

### Linting
```bash
flake8 src/
black src/
```
