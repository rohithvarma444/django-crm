# Django CRM - Customer Relationship Management System

A simple and modern Customer Relationship Management (CRM) system built with Django. This project helps you manage customer records, track leads, and maintain business relationships efficiently.

## 🚀 Features

- **User Authentication**: Secure login, registration, and logout system
- **Customer Records Management**: Add, view, and manage customer information
- **Responsive Design**: Modern Bootstrap-based UI that works on all devices
- **Message System**: Real-time feedback for user actions
- **CSRF Protection**: Secure form handling with Django's built-in CSRF protection

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- MySQL database (as configured in settings.py)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd django-crm
```

### 2. Create Virtual Environment
```bash
python3 -m venv virt
source virt/bin/activate  # On macOS/Linux
# or
virt\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
Make sure your MySQL database is running and update the database settings in `dcrm/settings.py` if needed:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elderco',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

### 5. Run Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python3 manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python3 manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
django-crm/
├── dcrm/                    # Main Django project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── website/                # Main app directory
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── apps.py
│   ├── forms.py           # User registration form
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── tests.py
│   └── templates/         # HTML templates
│       ├── base.html      # Base template
│       ├── home.html      # Home page template
│       ├── login.html     # Login template
│       ├── register.html  # Registration template
│       └── navbar.html    # Navigation bar
├── manage.py              # Django management script
└── README.md             # This file
```

## 🗄️ Database Models

### Record Model
The main model for storing customer information:

- `first_name`: Customer's first name (max 20 characters)
- `last_name`: Customer's last name (max 20 characters)
- `email`: Customer's email address (max 20 characters)
- `phone`: Customer's phone number (max 20 characters)
- `address`: Customer's address (max 100 characters)
- `city`: Customer's city (max 20 characters)
- `state`: Customer's state (max 20 characters)
- `zipcode`: Customer's zip code (max 20 characters)
- `created_at`: Timestamp when record was created (auto-generated)

## 🔐 Authentication System

### User Registration
- Users can register with username, email, first name, and last name
- Password validation ensures security
- Automatic login after successful registration

### User Login
- Secure authentication using Django's built-in auth system
- Session management
- Redirect to home page after successful login

### User Logout
- Secure logout with session cleanup
- Redirect to home page with success message

## 🎨 User Interface

### Bootstrap Integration
- Modern, responsive design using Bootstrap 5
- Mobile-friendly interface
- Professional color scheme and typography

### Navigation
- Dynamic navbar that changes based on authentication status
- User dropdown menu with profile options
- Clean and intuitive navigation

### Message System
- Success messages (green alerts)
- Error messages (red alerts)
- Warning messages (yellow alerts)
- Info messages (blue alerts)
- Dismissible alerts with close buttons

## 🚀 Usage Guide

### 1. First Time Setup
1. Register a new account using the registration form
2. Log in with your credentials
3. You'll be redirected to the home page with customer records

### 2. Viewing Records
- After logging in, you'll see a table of all customer records
- Records display: Name, Email, Phone, Address, City, State, Zipcode, Created Date, and ID
- Records are sorted by creation date (newest first)

### 3. Adding Records (Future Feature)
- Currently, records need to be added via Django admin or database
- Future versions will include a form to add new records

### 4. User Management
- Use the dropdown menu in the navbar to access user options
- Logout securely when done

## 🔧 Configuration

### Environment Variables
You can customize the following settings in `dcrm/settings.py`:

- `DEBUG`: Set to `False` for production
- `SECRET_KEY`: Change for production deployment
- `ALLOWED_HOSTS`: Add your domain for production
- Database settings: Update connection details as needed

### Static Files
Static files are served from the `static/` directory. For production, configure your web server to serve static files.

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL is running
   - Check database credentials in settings.py
   - Verify database exists

2. **Migration Errors**
   - Delete migration files and recreate them
   - Run `python3 manage.py makemigrations --empty website`
   - Then run `python3 manage.py makemigrations`

3. **CSRF Token Errors**
   - Ensure `{% csrf_token %}` is in all forms
   - Check that `CsrfViewMiddleware` is enabled in settings

4. **Template Errors**
   - Verify all template files exist
   - Check template syntax and indentation
   - Ensure proper template inheritance

## 📝 Contributing

This is a learning project. Feel free to:
- Add new features
- Improve the UI/UX
- Fix bugs
- Add more comprehensive documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Next Steps

Future enhancements could include:
- Add/Edit/Delete customer records
- Search and filter functionality
- Export data to CSV/PDF
- Email integration
- Task management
- Sales tracking
- Dashboard with analytics
- API endpoints for mobile apps

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review Django documentation
3. Check the project structure and configuration

---

**Happy Coding! 🚀**

This is your first Django project - congratulations on building a functional CRM system! Keep learning and building amazing applications. 