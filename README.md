
# Game API

This is a simple game API built using Django REST Framework. Players can answer quiz questions and track their score and streaks.

## Base URL
`http://127.0.0.1:8000/`

---

## Endpoints

### 1. List All Questions
**GET /questions/**

This endpoint retrieves all available questions in the game.

#### Request

- Method: `GET`
- URL: `/questions/`

#### Response

- **200 OK**
    - Returns a list of all questions in the database.

#### Example Response:
```json
[
    {
        "id": 1,
        "question_text": "What is the capital of France?",
        "answer": "Paris",
        "difficulty": 1
    },
    {
        "id": 2,
        "question_text": "What is the largest planet in the solar system?",
        "answer": "Jupiter",
        "difficulty": 2
    }
]
```

---

### 2. Retrieve a Specific Question
**GET /questions/{id}/**

This endpoint retrieves a specific question by its ID.

#### Request

- Method: `GET`
- URL: `/questions/{id}/`

#### URL Parameters:
- `id` (integer): The ID of the question you want to retrieve.

#### Response

- **200 OK**
    - Returns the details of the requested question.
- **404 Not Found**
    - If the question does not exist.

#### Example Response:
```json
{
    "id": 1,
    "question_text": "What is the capital of France?",
    "answer": "Paris",
    "difficulty": 1
}
```

---

### 3. Submit an Answer
**POST /sessions/{question_id}/answer/**

This endpoint allows a player to submit an answer for a specific question.

#### Request

- Method: `POST`
- URL: `/sessions/{question_id}/answer/`

#### URL Parameters:
- `question_id` (integer): The ID of the question for which the answer is being submitted.

#### Body Parameters:
- `player_id` (string): The unique identifier for the player submitting the answer.
- `answer` (string): The answer submitted by the player.

#### Response

- **200 OK**
    - Returns whether the answer was correct or not, and updates the player's score and streak.
- **400 Bad Request**
    - If `player_id` or `answer` is missing.
- **404 Not Found**
    - If the question does not exist.

#### Example Request:
```json
{
    "player_id": "player123",
    "answer": "Paris"
}
```

#### Example Response (Correct Answer):
```json
{
    "answered_correctly": true,
    "current_score": 10,
    "streak": 1
}
```

#### Example Response (Incorrect Answer):
```json
{
    "answered_correctly": false,
    "current_score": 10,
    "streak": 0
}
```

---

### 4. List Game Sessions
**GET /sessions/**

This endpoint retrieves all game sessions where players have answered questions.

#### Request

- Method: `GET`
- URL: `/sessions/`

#### Response

- **200 OK**
    - Returns a list of all game sessions.

#### Example Response:
```json
[
    {
        "id": 1,
        "player": "player123",
        "question": "What is the capital of France?",
        "answered_correctly": true,
        "timestamp": "2024-10-10T12:00:00Z"
    },
    {
        "id": 2,
        "player": "player456",
        "question": "What is the largest planet in the solar system?",
        "answered_correctly": false,
        "timestamp": "2024-10-10T12:05:00Z"
    }
]
```

---

### 5. Retrieve a Specific Game Session
**GET /sessions/{id}/**

This endpoint retrieves a specific game session by its ID.

#### Request

- Method: `GET`
- URL: `/sessions/{id}/`

#### URL Parameters:
- `id` (integer): The ID of the game session.

#### Response

- **200 OK**
    - Returns the details of the requested game session.
- **404 Not Found**
    - If the game session does not exist.

#### Example Response:
```json
{
    "id": 1,
    "player": "player123",
    "question": "What is the capital of France?",
    "answered_correctly": true,
    "timestamp": "2024-10-10T12:00:00Z"
}
```

---

### 6. List All Players
**GET /players/**

This endpoint retrieves all players in the game.

#### Request

- Method: `GET`
- URL: `/players/`

#### Response

- **200 OK**
    - Returns a list of all players and their current scores and streaks.

#### Example Response:
```json
[
    {
        "player_id": "player123",
        "score": 50,
        "streak": 3
    },
    {
        "player_id": "player456",
        "score": 20,
        "streak": 1
    }
]
```

---

### 7. Retrieve a Specific Player
**GET /players/{player_id}/**

This endpoint retrieves a specific player by their `player_id`.

#### Request

- Method: `GET`
- URL: `/players/{player_id}/`

#### URL Parameters:
- `player_id` (string): The unique identifier for the player.

#### Response

- **200 OK**
    - Returns the details of the requested player.
- **404 Not Found**
    - If the player does not exist.

#### Example Response:
```json
{
    "player_id": "player123",
    "score": 50,
    "streak": 3
}
```

---

### 8. Create a New Question
**POST /questions/**

This endpoint allows you to create a new question for the game.

#### Request

- Method: `POST`
- URL: `/questions/`

#### Body Parameters:
- `question_text` (string): The text of the question.
- `answer` (string): The correct answer to the question.
- `difficulty` (integer): The difficulty level of the question (1: easy, 2: medium, 3: hard).

#### Response

- **201 Created**
    - Returns the newly created question.
- **400 Bad Request**
    - If required fields are missing or invalid.

#### Example Request:
```json
{
    "question_text": "What is the capital of Japan?",
    "answer": "Tokyo",
    "difficulty": 1
}
```

#### Example Response:
```json
{
    "id": 3,
    "question_text": "What is the capital of Japan?",
    "answer": "Tokyo",
    "difficulty": 1
}
```

---

## Error Codes

- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created.
- **400 Bad Request**: The request had missing or invalid fields.
- **404 Not Found**: The requested resource was not found.
