# Create_Superuser-using-Django
Django web application with a custom user authentication system

# Configuration in settings.py
# Static Files
Django uses the static module to handle static files (CSS, JavaScript, images). 
The configuration includes:

# STATIC_URL: 
The URL to use when referring to static files located in STATICFILES_DIRS.

# STATICFILES_DIRS: 
Directories (other than STATIC_ROOT) where Django will look for static files.

# STATIC_ROOT: 
The directory where collectstatic will gather all static files for production use.

# Custom User Model
Django allows you to specify a custom user model by setting AUTH_USER_MODEL. 
This is useful when the default User model does not meet your requirements. 
In this case, accounts.GFG is used as the custom user model.

# Form Handling
SuperuserCreationForm
This form (SuperuserCreationForm) extends forms.
ModelForm, which is a class provided by Django to create forms tied to a database model.

# password: 
This field uses forms.CharField with a widget=forms.
PasswordInput to ensure the password is masked when typed.
Meta: This inner class specifies the model (GFG) and the fields to include in the form.

# save(): 
The save method is overridden to handle setting the password correctly and ensuring the user is marked as a superuser and staff member.

# Views
# create_superuser View
This view handles the display and processing of the superuser creation form.

# GET Request: 
If the request is a GET request, it renders the form.
 # POST Request: 
If the request is a POST request, it processes the form data. If the form is valid, it creates the superuser and displays a success message.
Messages Framework: Django's messages framework is used to provide feedback to the user.
URLs.

# accounts/urls.py
This file maps URLs to views. The create_superuser view is mapped to #accounts/create_superuser/.

# Template
# create_superuser.html
This HTML file is the template for the superuser creation page.

# {% load static %}: 
This tag loads the static files template tags, which are necessary to use {% static %}.
Form Rendering: The form is rendered using {{ form.as_p }}, which outputs each form field as a paragraph.

# CSRF Token: 
{% csrf_token %} is necessary for protecting the form against Cross-Site Request Forgery attacks.
Messages: Displays any messages from the messages framework.

# CSS
# styles.css
This file contains basic CSS to style the superuser creation form. 
It includes styles for the body, container, form elements, and buttons.

# Collect Static Files
# collectstatic Command
Running  
# """python manage.py collectstatic """ 
gathers all static files from STATICFILES_DIRS and app directories into STATIC_ROOT. 
This is particularly useful for deployment, ensuring all static files are in one place.

# Running the Development Server
# python manage.py runserver
This command starts the Django development server, allowing you to test your application locally.

# Superuser Creation Page
# Accessing the Page
# Navigate to http://127.0.0.1:8000/accounts/create_superuser/ 
to access the superuser creation form. 
This form allows you to create superusers directly from the web interface.

# Summary
Project Structure: Organizes static files, templates, views, and models for maintainability.
Static Files Configuration: Sets up handling of static files using static module.
Custom User Model: Allows customization of the user model to suit specific requirements.
Form Handling: Uses Django forms to handle user input and create superusers.
View Logic: Handles form display and processing, using Django’s messages framework for feedback.
URL Mapping: Connects URLs to views, ensuring the correct view handles each URL.
Template Rendering: Uses Django template language to render forms and include static files.
Styling: Applies CSS to style the form, improving user experience.
Static File Collection: Gathers all static files for easy deployment.
Local Testing: Runs a local server to test the application.
