# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class 123(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_123(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Ahyra0003")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text(u"Gerenciar Cães").click()
        driver.find_element_by_link_text(u"Adicionar Cão").click()
        driver.find_element_by_id("id_Nome").clear()
        driver.find_element_by_id("id_Nome").send_keys("Tereso")
        driver.find_element_by_id("id_Idade").clear()
        driver.find_element_by_id("id_Idade").send_keys("1")
        driver.find_element_by_name("Foto").clear()
        driver.find_element_by_name("Foto").send_keys("C:\\Users\\roger\\Desktop\\Recursos\\photo_dica2.png")
        driver.find_element_by_name("Info").clear()
        driver.find_element_by_name("Info").send_keys("Um bom cachorro.")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text("Sair").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
