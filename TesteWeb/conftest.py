import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bsbwebhomo.sarah.br/catalogoSistemas/#/")
    driver.maximize_window()
