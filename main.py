import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time #Para ver los movimientos

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
    button_taxi = (By.CLASS_NAME, 'button round')                               #botón pedir taxi
    button_confort = (By.XPATH, "//button[@data-for='tariff-card-4']")          #botón confort
    button_tel = (By.CLASS_NAME, 'np-button')                                   #botón para modal de teléfono
    phone_field = (By.ID, 'phone')                                              #input de no. tel
    button_regis_tel = (By.XPATH, "//button[normalize-space()='Siguiente']")    #Botón siguiente del modal tel
    codi_tel_field = (By.CSS_SELECTOR, "input#code[placeholder='xxxx']")        #input código tel
    button_confirm_codi = (By.XPATH, "//button[normalize-space()='Confirmar']") #botón para confirmar código
    button_pp = (By.CLASS_NAME, 'pp-text')                                      #botón método de pago
    button_pp_tarjeta = (By.XPATH, "//div[contains(@class, 'pp-title') "
                                   "and normalize-space()='Agregar tarjeta']")  #botón agregar tarjeta
    number_card_field = (By.ID, 'number')                                       #input numero de tarjeta
    codi_card_field = (By.CSS_SELECTOR, "input#code[placeholder='12']")         #input código de tarjeta
    button_regis_card = (By.XPATH, "//button[@type='submit' "
                                   "and normalize-space()='Agregar']")          #botón registrar tarjeta
    button_close_modal = (By.CSS_SELECTOR,
                     ".payment-picker .section.unusual button.section-close")   #botón para cerrar modal
    comment_field = (By.ID, 'comment')                                          #input de comentario
    input_check_MP = (By.XPATH,
        "//div[contains(@class,'r-sw-container')]"
        "[.//div[contains(@class,'r-sw-label') and "
        "normalize-space()='Manta y pañuelos']]//input[@type='checkbox']")      #Activar las mantas y pañuelos
    inc_count_ice = (By.XPATH,
        "//div[contains(@class,'r-counter-container')]"
        "[.//div[contains(@class,'r-counter-label') and "
        "normalize-space()='Helado']]//div[contains(@class,'counter-plus')]")   #Incrementar cantidad de helados
    smart_button = (By.CLASS_NAME, 'smart-button')                              #botón para iniciar

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def click_pedir_taxi(self): #Clic del botón pedir taxi
        self.driver.find_element(*self.button_taxi).click()

    def click_confort(self): #Clic del botón confort
        self.driver.find_element(*self.button_confort).click()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def wait_for_load_from(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.wait_for_load_from()
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        # time.sleep(3)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
