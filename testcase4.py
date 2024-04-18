from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir una página web
driver.get("https://www.saucedemo.com/")

# Ingresar datos incorrectos en el formulario de inicio de sesión
username = "usuario_incorrecto"
password = "contraseña_incorrecta"

# Escribir el nombre de usuario y la contraseña en los campos correspondientes
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# Hacer clic en el botón de inicio de sesión
driver.find_element(By.ID, "login-button").click()

# Esperar a que aparezca el mensaje de error
error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

# Verificar que el mensaje de error es correcto
assert error_message.text == "Epic sadface: Username and password do not match any user in this service", "Error: Mensaje de error incorrecto"

print("Inicio de sesión fallido debido a datos incorrectos")

# Cerrar el navegador
driver.quit()
