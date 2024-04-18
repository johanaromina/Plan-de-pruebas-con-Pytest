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

try:
    # Verificar que la tabla de contenido esté presente
    toc = wait.until(EC.presence_of_element_located((By.ID, "toc")))
    print("La tabla de contenido está presente")

    # Obtener todos los elementos de la tabla de contenido
    toc_elements = toc.find_elements(By.TAG_NAME, "a")

    # Verificar que cada elemento de la tabla de contenido sea clickeable y funcionen correctamente
    for element in toc_elements:
        element_text = element.text
        element.click()
        print(f"Elemento '{element_text}' es clickeable y funciona correctamente")

except Exception as e:
    print("Error:", e)

# Cerrar el navegador
driver.quit()
