# TigerLab Python Intern Assessment

## Requirements
* Python 3.9.X  

## Steps
1. Clone Repository
2. Change directory into the repo
3. Create a new venv  
```python -m venv ./venv```
4. Enter the new virtual environment  
```source venv/scripts/activate```
5. Install requirements.txt  
```pip install requirements.txt```
6. Create your superuser for the app  
```python manage.py createsuperuser```
7. Create `media` directory  
```mkdir media```
8. Perform migrations  
`python manage.py makemigrations`  
`python manage.py migrate`
9. Run Server  
`python manage.py runserver`

## Optional
Generate your secret key and replace the default secret key located in `secrets.json`.  

Run the following line of code in terminal and copy the result  
```python -c "from django.core.management import utils; print(utils.get_random_secret_key())"```  
Note: you will have to run the code in environment installed with django