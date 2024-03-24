#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class PersonData:
    # Данные для первого пользователя
    user_name = 'Ильина Виталина'
    login = 'vitalina_ilin@test.ru'
    password = 'VitaliyPass123_'

class ValidData:
    # Данные для второго пользователя
    user_name = 'Тест Тестов'
    login = f"test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"