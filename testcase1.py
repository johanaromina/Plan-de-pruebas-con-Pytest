from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Inicializar el navegador

driver= webdriver.Chrome ()

# Abrir una página web

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()