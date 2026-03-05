import os
from flask import Flask, jsonify
from flasgger import Swagger
from dal.csv_reader import CSVReader
from dal.db_repository import DBRepository
from dal.db_models import DBModels
from dal import engine
from bll.course_service import CourseService
from generator.csv_generator import CSVGenerator


app = Flask(__name__)
swagger = Swagger(app)

@app.post("/generate-csv/<int:num_rows>")
def generate_csv(num_rows: int):
    """
    Generate a CSV file with the specified number of rows.
    ---
    parameters:
      - name: num_rows
        in: path
        type: integer
        required: true
        description: The number of rows to generate in the CSV file.
    responses:
        200:
            description: CSV file generated successfully.
        400:
            description: Invalid input, number of rows must be at least 1000.
    """
    if num_rows < 1000:
        return jsonify({"error": "Minimum number of rows is 1000."}), 400
    generator = CSVGenerator(filename="courses.csv", num_rows=num_rows)
    generator.generate_csv()
    return jsonify({"message": f"CSV file generated with {num_rows} rows in ./data/."})


@app.post("/create-database")
def create_database():
    """
    Create the database and import data from the CSV file.
    ---
    responses:
        200:
            description: Database created and data imported successfully.
        400:
            description: CSV file not found. Please generate the CSV file first.
    """
    filename = "data/courses.csv"
    if not os.path.exists(filename):
        return jsonify({"error": "CSV file not found. Please generate the CSV file first."}), 400
    csv_reader = CSVReader(filename)
    data = csv_reader.read_csv()
    db_repository = DBRepository(engine, data)
    db_models = DBModels(engine)

    service = CourseService(csv_reader, db_models, db_repository)
    service.create_tables()
    service.import_data()
    return jsonify({"message": "Database created and data imported successfully."})


if __name__ == "__main__":
    app.run(debug=True)