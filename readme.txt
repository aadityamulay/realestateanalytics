Real Estate Data Analytics Project
Overview
This project simulates and analyzes real estate data using Python. It demonstrates key skills in data generation, database integration, analytics, and logging, making it relevant to real-world applications in the real estate domain.

Features
Data Generation
Generates synthetic data for properties (e.g., name, location, area, construction year, market value)
Creates market trends data for average prices over time
Configurable number of properties and date ranges
Database Integration
Inserts generated data into a MySQL database
Demonstrates basic SQL operations using Python's mysql.connector
Includes error handling and connection management
Data Analytics
Provides summary statistics for property data
Calculates average market values by location
Analyzes yearly market trends and visualizes them using Matplotlib
Logging System
Comprehensive logging of all major operations
Tracks data generation, database operations, and analytics processing
Logs stored in 'real_estate.log' with timestamps
Helps with debugging and monitoring system operation
Testing
Basic test suite implemented using pytest
Validates data generation and analytics functionality
Independent test cases for each major component
Requirements
Python 3.7+
MySQL database
Libraries:
numpy
pandas
matplotlib
mysql-connector-python
pytest
logging (standard library)
Installation
Clone the repository:
bash

Copy
git clone https://github.com/aadityamulay/real_estate_analytics
Install required libraries:
bash

Copy
pip install numpy pandas matplotlib mysql-connector-python pytest
Set up your MySQL database:
Create a database and tables using the schema in mysql final schema.sql
Update db_config in thisisthefinalrealestate.py with your MySQL credentials
Usage
Generate and Insert Data
Run the main script to generate property and market trend data and insert it into the database:

bash

Copy
python thisisthefinalrealestate.py
Monitor Operations
Check real_estate.log for operation logs
Logs include timestamps and operation status
Critical errors and warnings are automatically logged
Perform Analytics
The script performs analytics and visualizes results including:

Property distribution by location
Market trends over time
Results displayed on console and as plots
Run Tests
Execute the test suite to validate functionality:

bash

Copy
pytest
File Structure
thisisthefinalrealestate.py: Core logic for data generation, database integration, and analytics
simple_tests.py: Basic test suite using pytest
mysql final schema.sql: SQL script for database schema setup
real_estate.log: Operation logs (automatically generated)
Future Improvements
Incorporate real-world datasets for analytics
Add predictive modeling for market trends
Create a web-based dashboard for interactive analytics
Enhance testing to include database error handling and edge cases
Add more detailed logging for specific operations
Implement log rotation for long-term operation
Author
@Aditya Mulay

License
This project is open source and available under the MIT License.

