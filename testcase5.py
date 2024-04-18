from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://www.saucedemo.com/")

# Esperar a que todos los elementos estén presentes en la página
wait = WebDriverWait(driver, 10)

# Verificar que todas las imágenes estén presentes y visibles
images = driver.find_elements(By.TAG_NAME, "img")
for image in images:
    assert image.is_displayed(), "Error: La imagen no está visible"

print("Todas las imágenes están cargadas correctamente")

# Verificar que todos los textos estén presentes y visibles
text_elements = driver.find_elements(By.XPATH, "//*[not(self::script or self::style)]/text()[normalize-space()]")
for text_element in text_elements:
    assert text_element.is_displayed(), "Error: El texto no está visible"

print("Todos los textos están cargados correctamente")

# Cerrar el navegador
driver.quit()
