# Instructions How to Install and Run Locally

## Prerequisites(required)

| Name   | Required version(s) |
|----------|:-------------:|
| Python |  3.7 or higher | 
| Django |  3.1 or higher  |  

## Upgrade your Python pip to the latest version 

> First of all, please verify that your Python pip is already upgrade to the latest version. The commands to upgrade Python pip for Linux and MacOS usually are `python3` and `pip3`, different from other operating system that are `python` and `pip`.

Perform this command to upgrade Python pip

* #### Windows
```
    python -m pip install --upgrade pip
```

* #### Linux/MacOS
```
    python3 -m pip install --upgrade pip
```

## Install virtualenv

> You can run Python apps in a virtual environment that contains a separate, stand-alone copy of Python and all the Python add-ons that the application requires. You can read more information about virtualenv at [How to use virtualenv](https://cpske.github.io/ISP/django/virtualenv).

In order to create isolated lightweight Python environments, please install virtualenv by perform this command.

* #### Windows

```
    python -m pip install virtualenv
```

* #### Linux/MacOS

```
    python3 -m pip install virtualenv
```

## Installation Steps

### 1. Clone DEK-COM repository to your local machine

   > There are 2 ways to download the code to your local machine. You can either download the code as a ZIP file or open the terminal and follow the command below.

Before perform commands below, please navigate to the directory that you want to store the code by using this command `cd <your target directory>`

```
    git clone https://github.com/Jomsaruj/DEK-COM.git
```
### 2. Navigate to the project directory
```
        cd DEK-COM
```

### 3. Create isolated lightweight Python environments

   * #### Windows
```
    virtualenv env
```
* #### MacOs/Linux

```
    virtualenv venv
```

### 4. Activate virtualenv

* #### Windows
```
    env\Scripts\activate
```
* #### Linux/MacOS

```
    source venv/bin/activate
```
### 5. Install all required software included in `requirements.txt`

```
    pip install -r requirements.txt
```

### 6. Renaming the configuration file
> There are `sample.env` file that contain sample configuration for env variables. Rename `sample.env` to `.env` before running migrations.
* #### Windows
```
    move sample.env .env
```
* #### Linux/MacOS
```
    mv sample.env .env
```

### 7. Running migrations
#### Please ignore a WARNING in this step.
* #### Windows
```
    python manage.py migrate
```
* #### Linux/MacOS
```
    python3 manage.py migrate
```
### 8. Import data from file `users.json` to initiate initial user accounts.
#### Please ignore a WARNING in this step.
* #### Windows
```
    python manage.py loaddata users.json
```
* #### Linux/MacOS
```
    python3 manage.py loaddata users.json
```

### 9. Run the server
* #### Windows

```
    python manage.py runserver
```
* #### Linux/MacOS

```
    python3 manage.py runserver
```

### 10. Login to DEK-COM web application using demo account

| Account   | Username | Password|
|----------|-------------|:----------:|
| account 1 |  myusername | mypassword|
| account 2 |  yourusername  | yourpassword  |

### 11. Deactivate virtualenv

```
        deactivate 
```
