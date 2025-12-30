# Todo-List
TO-DO LIST WEB APPLICATION USING DJANGO AND POSTGRESQL

1. INTRODUCTION
In today’s fast-paced digital world, task management plays an important role in improving productivity. A To-Do List application helps users organize, track, and manage their daily activities efficiently. Web-based applications make task management more accessible by allowing users to manage tasks from any device with internet access.
This project involves the development of a To-Do List Web Application using Django (Python framework), developed in Visual Studio Code, and connected to a PostgreSQL database for data storage.

2. PROBLEM STATEMENT
Many individuals face difficulties in managing their daily tasks due to lack of proper tools or systems. Traditional methods such as notebooks are inefficient and prone to loss. There is a need for a simple, reliable, and user-friendly web application that allows users to manage tasks digitally with proper data storage.

3. OBJECTIVES
The main objectives of this project are:
To develop a simple and efficient To-Do List web application
To implement CRUD operations (Create, Read, Delete)
To understand Django’s MVT architecture
To connect Django with PostgreSQL database
To gain hands-on experience in backend web development

4. SYSTEM REQUIREMENTS
Hardware Requirements
Laptop or Desktop
Minimum 4 GB RAM
Internet connection
Software Requirements
Python
Django Framework
PostgreSQL Database
Visual Studio Code
Web Browser (Chrome/Edge)

5. TECHNOLOGIES USED
Frontend: HTML, CSS
Backend: Python (Django)
Database: PostgreSQL
IDE: Visual Studio Code

6. SYSTEM ARCHITECTURE
The application follows Django’s MVT (Model-View-Template) architecture:
Model: Defines the database structure for tasks
View: Contains business logic to process user requests
Template: Displays data to users using HTML
Database: PostgreSQL stores task details persistently

7. MODULE DESCRIPTION
7.1 Task Module
Add new tasks
Display all tasks
Delete existing tasks
7.2 Database Module
Stores task information
Uses PostgreSQL with Django ORM
Ensures secure and reliable data storage

8. DATABASE DESIGN
The database contains a table for tasks with fields such as:
Task ID
Task Title
Created Date
Django ORM automatically creates and manages database tables using migrations.

9. IMPLEMENTATION
The project is implemented using Django’s built-in features such as:
URL routing
Views and templates
Forms for user input
ORM for database operations
PostgreSQL for backend storage
Users can add tasks through a web form, view all tasks on the homepage, and delete completed tasks.

10. RESULTS
The To-Do List application works successfully by:
Allowing users to add tasks
Displaying stored tasks from PostgreSQL
Deleting tasks when required
Maintaining data persistence across sessions

11. ADVANTAGES
Easy to use
Secure database storage
Scalable web application
Uses industry-standard technologies
Reduces manual task management

12. LIMITATIONS
No user authentication
No task update feature
Single-user application

13. FUTURE ENHANCEMENTS
Add user login and authentication
Implement task update and priority levels
Add deadline and reminder features
Improve UI with Bootstrap
Deploy application on cloud

14. CONCLUSION
This project successfully demonstrates the development of a To-Do List web application using Django and PostgreSQL. It provides practical exposure to web development concepts, database connectivity, and Django framework features. The project is suitable for beginners and helps build a strong foundation in backend development.