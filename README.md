# FastAPI Blog Authentication (Basic)

A simple **FastAPI** blog application that demonstrates **authentication** using basic token-based authentication. It includes user registration, login functionality, and the ability to manage blog posts.

## Features

- **User Authentication**: Register and login users with basic authentication
- **JWT Token**: Secure user authentication using JSON Web Tokens (JWT)
- **CRUD Operations for Blog Posts**: Create, Read, Update, and Delete blog posts
- **Pydantic Models**: Data validation for requests and responses

## Getting Started

### Prerequisites

- **Python 3.x** installed on your machine
- **Git** for cloning the repository
- **A virtual environment** setup

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/FastApi_Blog_Authentication_Basic.git
    cd FastApi_Blog_Authentication_Basic
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```

5. **Access the app in your browser:**
   Visit [http://localhost:8000](http://localhost:8000) to view the API and [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI documentation.

### Usage

- **User Registration**: Register a new user by sending a `POST` request to `/register/` with the following data:
  
    ```json
    {
      "username": "user123",
      "password": "password"
    }
    ```

- **User Login**: Login by sending a `POST` request to `/login/` with the username and password. It will return a JWT token for authentication.

    ```json
    {
      "username": "user123",
      "password": "password"
    }
    ```

    The response will contain a token:

    ```json
    {
      "access_token": "jwt_token_here",
      "token_type": "bearer"
    }
    ```

- **Create Blog Post**: Send a `POST` request to `/posts/` with the following data:

    ```json
    {
      "title": "Blog Title",
      "content": "Blog Content"
    }
    ```

- **Get All Blog Posts**: Send a `GET` request to `/posts/` to retrieve all blog posts.

- **Get Blog Post by ID**: Send a `GET` request to `/posts/{id}/` to fetch a specific blog post by ID.

- **Update Blog Post**: Send a `PUT` request to `/posts/{id}/` with updated data:

    ```json
    {
      "title": "Updated Title",
      "content": "Updated Content"
    }
    ```

- **Delete Blog Post**: Send a `DELETE` request to `/posts/{id}/` to delete a blog post.

## Project Structure

- `main.py`: The main entry point for the FastAPI app, route definitions, and authentication logic.
- `models.py`: SQLAlchemy models for users and blog posts.
- `schemas.py`: Pydantic models for user registration, login, and blog post operations.
- `requirements.txt`: List of dependencies for the project.

## Contributing

Contributions are welcome! Feel free to submit a pull request to enhance functionality or fix bugs.
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
