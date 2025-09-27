# API Documentation

## Base URL
```
http://localhost:5000
```

## Endpoints

### GET /
- **Description**: Health check endpoint
- **Response**: Server status message

### POST /submit_landing
- **Description**: Submit initial patient information
- **Request Body**:
  ```json
  {
    "age": "number",
    "sex": "string",
    "location": "string"
  }
  ```
- **Response**:
  ```json
  {
    "question": "string",
    "question_type": "number"
  }
  ```

### POST /submit_info
- **Description**: Submit additional patient information
- **Request Body**:
  ```json
  {
    "user_id": "string",
    "info_inputs": "object"
  }
  ```
- **Response**:
  ```json
  {
    "statement": "string",
    "statement_type": "number"
  }
  ```

### POST /submit_answer
- **Description**: Submit answer to questionnaire
- **Request Body**:
  ```json
  {
    "user_id": "string",
    "answer": "string"
  }
  ```
- **Response**:
  ```json
  {
    "statement": "string",
    "statement_type": "number",
    "next": "string"
  }
  ```

### GET /get_result
- **Description**: Get final matching results
- **Query Parameters**:
  - `user_id`: User session identifier
- **Response**: Array of matched clinical trials
