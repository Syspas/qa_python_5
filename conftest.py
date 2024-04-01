#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data.data import PersonData
from data.urls import Urls
from web_locators.locators import *

# Получение значения переменной окружения GECKODRIVER_PATH и сохранение в переменной geckodriver_path
geckodriver_path = os.getenv("GECKODRIVER_PATH")

# Получение значения переменной окружения FIREFOX_BINARY_PATH и сохранение в переменной firefox_binary_path
firefox_binary_path = os.getenv("FIREFOX_BINARY_PATH")

# Декоратор для создания фикстуры в pytest
@pytest.fixture
# Определение функции-фикстуры firefox_driver
def driver():
# Создание объекта FirefoxBinary с указанием пути к исполняемому файлу Firefox
    binary = FirefoxBinary(firefox_binary_path)

# Создание объекта опций для браузера Firefox
    options = webdriver.FirefoxOptions()

# Установка режима headless (без графического интерфейса)
    options.headless = True


# Создание объекта драйвера для браузера Firefox с указанием пути к geckodriver, объекта FirefoxBinary и опциями
    driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_binary=binary, options=options)

# Возврат объекта драйвера для использования в тесте
    yield driver

# Закрытие браузера после завершения теста
    driver.quit()


@pytest.fixture
def login(driver):
    """ Вход в аккаунт """
    # Переход на страницу входа
    driver.get(Urls.url_login)

    # Заполнение полей электронной почты и пароля
    driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)

    # Нажатие кнопки входа
    driver.find_element(*AuthLogin.al_login_button_any_forms).click()

    # Ожидание появления кнопки заказа на главной странице
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPage.mn_order_button))


