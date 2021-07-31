## random_objects_project

REST API based on Flask. 
Have these functionalities:
  - Endpoint to generate a file of 2MB size(exceeds 2MB, approx. 2.1MB), which contains 4 types of random objects (alphabetical strings, real numbers, integers, alphanumerics).
  - Endpoint to download the generated file.
  - Endpoint to get a report of total number of each random object.

---

### Project Setup

- Python version supported: 3.8+

- Clone the project

  ```bash
  git clone git@github.com:adnan-alam/random_objects_project.git
  ```

- Install **virtualenv** if not installed on system

  ```bash
  # package to create virtual environment
  pip install virtualenv
  ```

- Go to dir **random_objects_project**, create a virtual environment **.env**

  ```bash
  virtualenv -p /usr/bin/python3.8 .env
  ```

  and activate it

  ```bash
  source .env/bin/activate
  ```

- Install all the dependencies

  ```bash
  pip install -r requirements.txt
  ```

- Run the development server

  ```bash
  python manage.py
  ```

  and the project will be served on `http://127.0.0.1:5000/`.

---

### API

#### Generate random objects' file

```http
  POST /api/v1/random-objects/generate
```

Request parameter: None

Response (JSON):

```bash
{
  "url": "/download/random_objects.txt"
}
```

#### Download generated file

```http
  GET /api/v1/download/<file_name>
```

Request parameter: None

Response: File

#### Get report of generated file

```http
  GET /api/v1/random-objects/report
```

Request parameter: None

Response (JSON):

```bash
# example

{
    "total_alphabetical_strings": 50659,
    "total_alphanumerics": 46807,
    "total_integers": 48352,
    "total_real_numbers": 48442
}
```
