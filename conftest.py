#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from web_locators.locators import *
from data.urls import Urls
from data.data import PersonData



@pytest.fixture
def driver():
    # Указание пути к исполняемому файлу Firefox
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # Настройка параметров браузера Firefox
    options = Options()
    options.binary = binary
    options.add_argument("--window-size=1920,1080")

    # Имя файла geckodriver.exe
    # Версия geckodriver-v0.34.0-win32 Версия браузера Mozilla Firefox 124.0.1 (64-разрядный)
    geckodriver_filename = 'geckodriver.exe'


    # Путь к geckodriver.exe
    geckodriver_path = os.path.join(os.getcwd(), geckodriver_filename)

    # Инициализация WebDriver для браузера Firefox с указанием пути к geckodriver.exe и передачей параметров
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)

    # Переход на URL главной страницы сайта
    driver.get(Urls.url_main_paige)

    yield driver

    # Закрытие WebDriver после завершения теста
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

    return driver