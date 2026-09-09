import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str | None:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code
    return code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.CSS_SELECTOR, '.button.round')
    button_confort = (By.CSS_SELECTOR, "div.tcard-icon "
                                "img[src='/static/media/kids.075fd8d4.svg']")
    text_card_active = (By.CSS_SELECTOR, 'div.tcard.active div.tcard-title')
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_field = (By.ID, 'phone')
    button_regis_tel = (By.XPATH, "//button[normalize-space()='Siguiente']")
    phone_code_field = (By.CSS_SELECTOR, "input#code[placeholder='xxxx']")
    button_confirm_code = (By.XPATH, "//button[normalize-space()='Confirmar']")
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, "//div[contains(@class, 'pp-title') "
                                   "and normalize-space()='Agregar tarjeta']")
    number_card_field = (By.ID, 'number')
    card_cvv_field = (By.CSS_SELECTOR, "input#code[placeholder='12']")
    payment_method = (By.CLASS_NAME, 'pp-value-text')
    button_regis_card = (By.XPATH, "//button[@type='submit' "
                                   "and normalize-space()='Agregar']")
    button_close_modal = (By.CSS_SELECTOR,
                     ".payment-picker .section.section.active "
                     "button.close-button.section-close")
    comment_field = (By.ID, 'comment')
    blanket_tissues = (By.XPATH,
        "//div[contains(@class, 'r-sw-label') "
        "and text()='Manta y pañuelos']/following-sibling::div//span")
    increase_ice_cream_count = (By.XPATH,
        "//div[contains(@class,'r-counter-container')]"
        "[.//div[contains(@class,'r-counter-label') and "
        "normalize-space()='Helado']]//div[contains(@class,'counter-plus')]")
    value_ice_cream_count = (By.XPATH,
        "//div[contains(@class,'r-counter-container')] "
        "[.//div[contains(@class,'r-counter-label') and normalize-space()='Helado']] "
        "//div[contains(@class,'counter-value')]")
    smart_button = (By.CSS_SELECTOR, 'button.smart-button')
    driver_info = (By.CLASS_NAME, "order-number")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        (WebDriverWait(self.driver, 10)
         .until(EC.visibility_of_element_located(self.from_field))
         .send_keys(from_address))

    def set_to(self, to_address):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.to_field))
         .send_keys(to_address))

    def set_phone(self, phone):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.phone_field))
         .send_keys(phone))

    def set_code(self, code):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.phone_code_field))
         .send_keys(code))

    def set_number_card_field(self, number_card):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.number_card_field))
         .send_keys(number_card))

    def set_card_cvv(self, codi_card):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.card_cvv_field))
         .send_keys(codi_card, Keys.TAB))

    def set_comment_field(self, comment):
        (WebDriverWait(self.driver,10)
         .until(EC.visibility_of_element_located(self.comment_field))
         .send_keys(comment))

    def click_pedir_taxi(self): #Clic del botón pedir taxi
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_taxi)).click())

    def click_confort(self): #Clic del botón confort
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_confort)).click())

    def click_button_tel(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.phone_button)).click())

    def click_button_regis_tel(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_regis_tel)).click())

    def click_button_confirm_code(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_confirm_code)).click())

    def click_payment_method_button(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.payment_method_button)).click())

    def click_add_card_button(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.add_card_button)).click())

    def click_button_regis_card(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_regis_card)).click())

    def click_button_close_modal(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.button_close_modal)).click())

    def click_blanket_tissues(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.blanket_tissues)).click())

    def click_increase_ice_cream_count(self, quantity):
        (WebDriverWait(self.driver, 10)
         .until(EC.element_to_be_clickable(self.increase_ice_cream_count)))
        for _ in range(quantity):
            self.driver.find_element(*self.increase_ice_cream_count).click()

    def click_smart_button(self):
        (WebDriverWait(self.driver,10)
         .until(EC.element_to_be_clickable(self.smart_button)).click())

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_text_card_active(self):
        return self.driver.find_element(*self.text_card_active).text

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def get_code(self):
        return self.driver.find_element(*self.phone_code_field).get_property('value')

    def get_number_card_field(self):
        return self.driver.find_element(*self.number_card_field).get_property('value')

    def get_card_cvv(self):
        return self.driver.find_element(*self.card_cvv_field).get_property('value')

    def get_payment_method(self):
        return self.driver.find_element(*self.payment_method).text

    def get_comment_field(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    def get_value_ice_cream(self):
        return self.driver.find_element(*self.value_ice_cream_count).text

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_phone_number(self, phone_number):
        self.click_button_tel()
        self.set_phone(phone_number)
        self.click_button_regis_tel()
        code = retrieve_phone_code(self.driver)
        self.set_code(code)
        self.click_button_confirm_code()
        assert self.get_code() == code

    def set_credit_card(self, number_card, card_cvv):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.set_number_card_field(number_card)
        self.set_card_cvv(card_cvv)
        assert self.get_number_card_field() == number_card
        assert self.get_card_cvv() == card_cvv
        self.click_button_regis_card()
        self.click_button_close_modal()

    def wait_for_load_from(self):
        (WebDriverWait(self.driver, 10)
         .until(EC.visibility_of_element_located(self.from_field)))

    def wait_for_load_driver(self):
        (WebDriverWait(self.driver, 60)
         .until(EC.visibility_of_element_located(self.driver_info)))

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)

    #1. Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #2. Seleccionar la tarifa Comfort.
    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pedir_taxi()
        routes_page.click_confort()
        assert routes_page.get_text_card_active() == 'Comfort'

    #3. Rellenar el número de teléfono.
    def test_field_number_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number.replace(' ', '')
        routes_page.set_phone_number(phone_number)
        assert routes_page.get_phone() == phone_number

    #4. Agregar una tarjeta de crédito.
    def test_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        number_card = data.card_number
        card_cvv = data.card_code
        routes_page.set_credit_card(number_card, card_cvv)
        assert routes_page.get_payment_method() == 'Tarjeta'

    #5. Escribir un mensaje para el controlador.
    def test_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        comment = data.message_for_driver[:24]
        routes_page.set_comment_field(comment)
        assert routes_page.get_comment_field() == comment

    #6. Pedir una manta y pañuelos.
    def test_select_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_tissues()

    #7. Pedir 2 helados
    def test_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_increase_ice_cream_count(2)
        assert routes_page.get_value_ice_cream() == '2'

    #8. Aparece el modal para buscar un taxi.
    def test_modal_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()

    #9. Esperar a que aparezca la información del conductor en el modal (opcional).
    def test_modal_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()