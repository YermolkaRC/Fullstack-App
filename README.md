# Fullstack-App, First try at using TS and React
One day I decided to switch from using Python for both backend and frontend to using something different. My choice was React with TypeScript, so this project is my first try at it. 
Based on React TS tutorial from https://handsonreact.com/docs/labs/react-tutorial-typescript

## Table of Contents
* [Prerequisites](#prerequisites)
* [Setup and Run](#setup-and-run)

## Prerequisites
* npm ~9.6.7
* Python 3.11 (Should work on older versions)

## Setup and Run
After cloning the project, install all other dependencies:

```
Frontend:
$ cd frontend
$ npm install

Backend:
$ cd backend
$ python -m venv venv

In VS Code terminal in Windows:
$ .\venv\Scripts\activate.ps1
On Linux:
$ source venv/Scripts/activate

$ pip install -r requirements.txt
```

To run backend:
Create a .env file with Flask and DB configuration. An example config for SQLite is inside example.env.
```
$ cd backend
$ python -m flask db upgrade
$ python app.py
```

To run frontend:
```
$ cd frontend
$ npm start
```
