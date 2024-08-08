# Bit: CSV Automation API

**Bit** is a lightweight tool designed to simplify the process of writing data to CSV files. This project aims to provide a local API that enables you to automate the task of updating CSV files with ease.

## Features

- **Local API Interface**: Communicate with Bit using HTTP requests to interact with your CSV files.
- **Easy Data Writing**: Quickly append new rows to your CSV files.
- **Dynamic File Handling**: Create or modify CSV files as needed.

## Installation

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SergiFuster/bit-project.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd bit-project
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   By default, the API will start on `http://localhost:5000`.

## Usage

### File Structure

Yo can create directories to match the default route:
```
data/
├── files/
```

Or change the route directly from ```main.py```:
```
drawer = "your_directory_path"
```

### API Endpoints

#### POST `/write`

**Description:** Append a new row of data to a CSV file.

**Request Body:**

- `file`: (string) Name of the CSV file (e.g., `data.csv`).
- `data`: (array) An array of values representing the row to be added.

**Example Request:**

```json
{
  "file": "data.csv",
  "data": ["John Doe", "johndoe@example.com", "123-456-7890"]
}
```

**Response:**

- **Success (200 OK):**

  ```json
  {
    "status": "success",
    "message": "Data written successfully."
  }
  ```

- **Error (400 Bad Request):**

  ```json
  {
    "status": "error",
    "message": "Invalid input or file not found."
  }
  ```

### Example Usage with `curl`

```bash
curl -X POST http://localhost:5000/write \
-H "Content-Type: application/json" \
-d '{"file": "data.csv", "data": ["Jane Smith", "janesmith@example.com", "098-765-4321"]}'
```

## Configuration

You can configure the API settings by modifying the `config.json` file in the project directory. This includes settings like the default file path and logging options.

## Testing

To ensure the application is working correctly, run the following command:

```bash
pytest
```

Make sure to add or modify tests in the `tests` directory as needed.

## Contributing

We welcome contributions to improve Bit! If you would like to contribute, please follow these steps:

1. **Fork the Repository**
2. **Create a New Branch** (`git checkout -b feature-branch`)
3. **Make Your Changes**
4. **Commit Your Changes** (`git commit -am 'Add new feature'`)
5. **Push to the Branch** (`git push origin feature-branch`)
6. **Create a Pull Request**

Please make sure your code adheres to the existing style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact sergifusterdura@gmail.com (mailto:sergifusterdura@gmail.com).

---

Thank you for using Bit! We hope it makes your CSV data management easier and more efficient.
