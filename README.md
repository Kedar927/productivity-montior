# Frontend Workspace Monitoring Application

This directory contains the frontend components of the Workspace Monitoring Application. The frontend is built using HTML, CSS, and JavaScript, and it interacts with the backend to provide real-time monitoring and logging features.

## Directory Structure

- **static/**: Contains static files such as CSS stylesheets.
- **templates/**: Contains HTML templates for rendering the web pages.

## Setup Instructions

1. Ensure you have a web server to serve the frontend files. You can use Flask's built-in server or any other web server of your choice.
2. Navigate to the `frontend` directory.
3. Open the `index.html` file in your web browser to view the application.

## Usage

- The application provides a user interface to monitor workspace entry and exit times.
- Users can log their lounge breaks and meeting durations.
- Real-time object detection is displayed at the entrance using YOLOv8.

## Features

- Real-time video feed from the entrance.
- Logging of entry times between 9 PM and 5 AM.
- Tracking of lounge breaks (10 to 15 minutes).
- Tracking of meeting times (30 minutes).

## Dependencies

Ensure that the necessary dependencies are installed in the backend, as the frontend interacts with the backend API for logging and monitoring functionalities.