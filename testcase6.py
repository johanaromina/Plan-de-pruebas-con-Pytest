from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://www.saucedemo.com/t")

# Esperar a que el formulario "Get A Quote" esté presente
form = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "requestaquote")))

# Llenar el formulario
driver.find_element(By.ID, "WhoWillBeFunding").send_keys("My employer")
driver.find_element(By.ID, "Name").send_keys("John Doe")
driver.find_element(By.ID, "CompanyEmail").send_keys("john.doe@example.com")
driver.find_element(By.ID, "Mobile").send_keys("1234567890")
driver.find_element(By.ID, "Message").send_keys("This is a test message")

# Hacer clic en el botón "Send enquiry"
driver.find_element(By.NAME, "send-request").click()

# Esperar a que se envíe el formulario (puedes agregar más verificaciones si es necesario)
WebDriverWait(driver, 10).until(EC.url_contains("/thank-you"))

print("Formulario enviado correctamente")

# Cerrar el navegador
driver.quit()
