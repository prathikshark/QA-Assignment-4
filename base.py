import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class TestAssesmentMethods:
    global chromedriver_path

    def __init__(self):
        options = Options()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.download_dir = os.path.join(current_dir, 'downloads')
        options.add_experimental_option('prefs', {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        })
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://benefits.plansourcetest.com")
        self.driver.maximize_window()
        time.sleep(3)

    def __action_double_click(self, data: str, skip=False):
        for option in self.driver.find_elements(By.TAG_NAME, "option"):
            if option.text == data:
                action_chains = ActionChains(self.driver)
                action_chains.double_click(option).perform()
                break

    def __click_right_arrow(self, select_id):
        self.driver.find_element(By.XPATH,
                                 f"//select[@id = '{select_id}']/parent::td/following-sibling::td/button").click()

    def __select_an_option(self, select_id: str, text: str):
        s = Select(self.driver.find_element(By.ID, select_id))
        s.select_by_visible_text(text)

    def read_file(self):
        # Get the latest file in the download directory
        files = os.listdir(self.download_dir)
        paths = [os.path.join(self.download_dir, basename) for basename in files]
        latest_file = max(paths, key=os.path.getctime)

    def admin_login(self):
        self.driver.find_element(By.ID, 'user_name').send_keys('nidavellir_admin')
        self.driver.find_element(By.ID, 'password').send_keys('automation1')
        login = self.driver.find_element(By.ID, 'logon_submit')
        login.click()
        time.sleep(3)

    def redirect_to_report(self):
        self.driver.get('https://benefits.plansourcetest.com/admin/report_benefit')
        time.sleep(3)

    def select_employee_status(self):
        self.driver.find_element(By.XPATH, "//button/span[contains(normalize-space(), 'Not Terminated')]").click()
        self.driver.find_element(By.LINK_TEXT, 'All Statuses').click()
        time.sleep(3)

    def select_checkbox(self):
        self.driver.find_element(By.XPATH, "//div/label[contains(text(), 'Unmask SSN')]").click()
        time.sleep(3)

    def select_plan_year(self, dates: str):
        self.__action_double_click(dates)
        time.sleep(3)

    def select_benefit_type(self, benefit_type: str):
        self.__action_double_click(data=benefit_type)
        time.sleep(5)

    def select_plans(self, plan_id: str, plan_type: str):
        self.__select_an_option(plan_id, plan_type)
        self.__click_right_arrow(plan_id)
        time.sleep(5)

    def select_available_plan_fields(self, plan_id: str, texts: list):
        for text in texts:
            self.__select_an_option(plan_id, text)
            self.__click_right_arrow(plan_id)
            time.sleep(2)

    def select_available_employee_fields(self, emp_field_id: str, texts: list):
        for text in texts:
            self.__select_an_option(emp_field_id, text)
            self.__click_right_arrow(emp_field_id)
            time.sleep(2)

    def run(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Run Report')]").click()
        time.sleep(2)

    def print_table_data(self):
        time.sleep(7)
        result = []

        all_headers = self.driver.find_elements(
            By.XPATH,
            "//table[@class='ps-table ps-table-header-no-top-border ps-table-grid ps-table-nowrap']/thead/tr/td"
        )

        XPATH = "//table[@class='ps-table ps-table-header-no-top-border ps-table-grid ps-table-nowrap']/tbody/tr"
        count = len(self.driver.find_elements(By.XPATH, XPATH))

        for i in range(1, count + 1):
            all_data_rows = self.driver.find_elements(By.XPATH, f"({XPATH})[{i}]/td")
            result.append(all_data_rows)

        for i in range(count):
            for idx in range(len(all_headers)):
                print(f"{all_headers[idx].text}: {result[i][idx].text}")
                print('\n\n\n\n')

        input()
