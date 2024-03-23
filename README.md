
# MyBookList

## Dockerized Flask API for Library Management

This Dockerized Flask API is designed to manage a library's collection of books, providing a suite of functionalities for adding, updating, retrieving, and deleting book records. It also includes additional endpoints for retrieving environment configuration data and generating Fibonacci sequences. The API is documented with Swagger UI for ease of use.

## My Journey

Starting with Spring Boot and Maven, guided by Amigoscode's tutorials on YouTube, I faced unexpected errors. This led me to pivot to Python and Flask, facilitating my project's development with its straightforward approach, thanks to helpful YouTube guides. Despite this shift, I aim to return to Spring Boot, believing in its value for my growth as a developer.

## Requirements

- Docker: For containerization of the application.
- Python: As the programming language for the Flask framework.
- Kubernetes: For deployment, scaling, and managing containerized applications.
- A Laptop or Desktop: To run and manage the application.

## Installation and Deployment

### Docker Deployment

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/HamimMahdie/MyBookList-main.git
   ```

2. **Build the Docker Image:**

   Inside the project directory:

   ```sh
   docker build -t my-flask-app .
   ```

3. **Run the Docker Container:**

   ```sh
   docker run -d -p 5002:5002 my-flask-app
   ```

4. **Access the API Documentation:**

   Visit [http://localhost:5002/swagger](http://localhost:5002/swagger) for the Swagger UI.

### Kubernetes Deployment

1. **Kubernetes Deployment:**

   Ensure the Docker image is in a registry your Kubernetes can access. Move to /manifests directory and execute the following-

   ```sh
   kubectl apply -f deployment.yaml
   ```

2. **Expose as a Kubernetes Service:**

   Apply the `service.yaml`:

   ```sh
   kubectl apply -f service.yaml
   ```

   Confirm the service is set with `type: NodePort`, mapping external to internal port `5002`.

3. **Access the Application:**

   Find your service's NodePort:

   ```sh
   kubectl get svc
   ```

   Access `http://<node-ip>:<node-port>/swagger`.

## API Endpoints

- **GET "/books"**: List all books.
- **POST "/books"**: Add a book.
- **GET "/books/<index>"**: Get a book.
- **PUT "/books/<index>"**: Update a book.
- **DELETE "/books/<index>"**: Delete a book.
- **GET "/config"**: Retrieve environment configuration data.
- **GET "/fib?length=n"**: Generate a sequence of `n` Fibonacci numbers.

Replace `<index>` with the book's index and `n` with the length for the Fibonacci sequence.
```
