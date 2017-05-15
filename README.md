# Heal demo

# Installation
The is a really basic test demo targeting a specific site and api.

***Note: The tests only setup the chromedriver currently. Add to setup.sh if you want to have it setup other drivers locally.***

    cd <directory_where_the_repo_was_cloned_to>
	make setup
If you receive a permissions error you may have to chmod a+x setup.sh .

# Usage
The setup task will install a virtualenv named healenv. When running tests be sure to source the the env.

```
source healenv/bin/activate
```

The tests use optional env vars at the moment to select the type of webdriver and or to use saucelabs to run remote tests.

| ENV VAR | Description |
| --- | --- |
| DRIVER | the flavor of driver to use at runtime. i.e. "chrome". See /tests/driver_factory.py |
| SAUCE | Bool to use saucelabs or not |
| SAUCE_USER | The saucelabs username to use |
| SAUCE_KEY | The saucelabs apikey to use |

The test are written in a manner to be ran with pytest or wrapped around pytest.

To run all the tests from the root directory:
```
pytest tests/
```
To run all the browser tests from the root directory:
```
pytest -m webtest tests/
```

To run all the api tests from the root directory:
```
pytest -m apitest tests/
```

# Adding more tests
The code generally consists of the standard page object pattern, a few utiliy functions, and is written to be used with pytest. pytest recognizes plain tests functions/methods and test classes derived from unittest.TestCase.
https://docs.pytest.org/en/latest/
http://selenium-python.readthedocs.io/page-objects.html

Add python dependencies to requirements.txt and rerun pip as needed.
```
pip install -r requirements.txt
```
Add other dependenices to the Makefile or setup.sh as needed.

#TODO
1. Add good logging or pipe to logstash from CI servers.
2. Extend with Cucumber or the Robot framework.
3. Dockerize for headless use with PhantomJS.
4. Make configurable with yaml files or dynamodb tables.
5. Test with mobile browsers/appium.
