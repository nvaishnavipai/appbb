Here's a structured and presentable `README.md` file for your Blood Bank Management Webpage:

---

# Blood Bank Management Webpage

This project is a web-based application for managing blood donors and recipients, built using Flask and MySQL. The system allows you to add, view, search, and delete records of donors and recipients, along with managing a blood inventory.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Routes](#routes)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Donor Management**: Add, view, search, and delete donor records.
- **Recipient Management**: Add, view, search, and delete recipient records.
- **Blood Inventory Management**: View the current blood inventory.
- **Eligibility Criteria**: Display blood donation eligibility criteria.
- **Search Functionality**: Search through donor and recipient records using different criteria.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- MySQL Server
- pip (Python package installer)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/blood-bank-management.git
   cd blood-bank-management
   ```

2. **Install Required Python Packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**

   - Create a MySQL database named `sample_database`.
   - Import the SQL file to set up tables:
     ```bash
     mysql -u root -p sample_database < database_schema.sql
     ```
   - Update the database configuration in `app.py` if necessary.

## Configuration

Update the following configurations in the `app.py` file according to your MySQL setup:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'sample_database'
```

## Usage

1. **Run the Flask Application:**

   ```bash
   python app.py
   ```

2. **Access the Application:**

   Open your browser and navigate to `http://localhost:5000` to access the Blood Bank Management system.

## Routes

- **Home**: `/` - View all donors.
- **Donor Management**: `/donormange` - Access donor management interface.
- **Add Donor**: `/adddonorpage` - Form to add a new donor.
- **Add Recipient**: `/addrecpage` - Form to add a new recipient.
- **View Blood Inventory**: `/bloodinv` - View blood inventory.
- **Eligibility Criteria**: `/elicri` - View blood donation eligibility criteria.
- **Search Donors**: `/search` (POST) - Search donors by name, phone, or blood group.
- **Search Recipients**: `/searchrec` (POST) - Search recipients by name, phone, or blood group.
- **Delete Donor**: `/delete/<id>` - Delete a donor by ID.
- **Delete Recipient**: `/deleterec/<id>` - Delete a recipient by ID.

## File Structure

```
├── templates
│   ├── home.html
│   ├── dman.html
│   ├── and.html
│   ├── anr.html
│   ├── index.html
│   ├── viewrec.html
│   ├── ec.html
│   └── ../static/binv.html
├── app.py
├── requirements.txt
└── README.md
```

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

