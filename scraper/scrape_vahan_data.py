from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import traceback
import time

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

try:
    print("🚀 Launching Chrome...")
    driver.get("https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml")
    print("🌐 Opened Vahan Dashboard")

    # 🔽 Custom dropdown selector for PrimeFaces
    def select_dropdown_by_id(dropdown_id, option_text):
        dropdown = wait.until(EC.element_to_be_clickable((By.ID, dropdown_id)))
        dropdown.click()
        time.sleep(1)

        menu_xpath = f"//ul[contains(@id, '{dropdown_id}_items')]/li[normalize-space(text())='{option_text}']"
        option = wait.until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
        option.click()
        print(f"✅ Selected '{option_text}' from '{dropdown_id}'")

    # 🟦 Select dropdowns
    select_dropdown_by_id("xaxisVar", "Vehicle Category Group")  # X-Axis
    select_dropdown_by_id("yaxisVar", "Vehicle Class")           # Y-Axis
    select_dropdown_by_id("selectedYearType", "Calendar Year")   # Year Type
    select_dropdown_by_id("selectedYear", "2025")                # Year

    # 🔁 Click Refresh (reliable fallback version)
    try:
        refresh_btn = wait.until(EC.element_to_be_clickable((By.ID, "j_idt45")))
        print("✅ Refresh button found by ID")
    except:
        refresh_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Refresh']")))
        print("✅ Refresh button found by fallback span text")

    refresh_btn.click()
    print("🔄 Clicked Refresh")

    # ⌛ Wait for table
    print("⌛ Waiting for table to load...")
    time.sleep(3)
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-datatable-data")))
    print("📊 Extracting table rows...")

    # 📥 Extract rows
    data = []
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        cols = [col.text.strip() for col in cols]
        if cols:
            data.append(cols)

    driver.quit()

    # 💾 Save to CSV
    columns = ["S.No", "Vehicle Class", "4WIC", "LMV", "MMV", "HMV", "Total"]
    df = pd.DataFrame(data, columns=columns)
    df.dropna(inplace=True)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_data.csv", index=False)
    print(f"✅ Scraped {len(df)} rows and saved to ➡️ data/raw_data.csv")

except Exception as e:
    print("❌ Error occurred:", str(e))
    traceback.print_exc()
    driver.quit()
