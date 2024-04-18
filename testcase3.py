from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir una página web
driver.get("https://www.saucedemo.com/")

# Ingresar datos correctos en el formulario de inicio de sesión
username = "standard_user"
password = "secret_sauce"

# Escribir el nombre de usuario y la contraseña en los campos correspondientes
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# Hacer clic en el botón de inicio de sesión
driver.find_element(By.ID, "login-button").click()

# Esperar a que la página de inicio de sesión se cargue completamente
WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

# Verificar que se haya iniciado sesión correctamente
assert "inventory.html" in driver.current_url, "Error: No se inició sesión correctamente"

print("Inicio de sesión exitoso")

# Cerrar el navegador
driver.quit()
