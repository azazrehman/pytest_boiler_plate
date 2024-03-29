# pytest_boiler_plate

### Setting up virtual environment

1 : Installing the virtualenv, use the below command to install the virtual env
``` 
pip install virtualenv  OR  python3 -m pip install virtualenv
 ```
2 : Creating virual environment in your project
```
python3 -m venv azaz_venv
```
3 : Activating your newly created virtual env
```
source azaz_venv/bin/activate   
```

### Installing the Requirement file

```
pip install -r requirements.txt
```

### Executing the tests
```
pytest src/tests/web --html-report=<Your_REPORT_NAME>