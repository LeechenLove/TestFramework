import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from Test_Framework.utils.config import Config, drivers_path, data_path,report_path
from Test_Framework.utils import logger
from Test_Framework.utils.file_reader import ExcelReader
from HTMLTestRunner import HTMLTestRunner
from Test_Framework.utils import Email

class TestBaidu(unittest.TestCase):
    url = Config().get('URL')
    excel = data_path + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=drivers_path + '\chromedriver.exe')
        self.driver.get(self.url)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()



if __name__ == "__main__":
    report  = report_path + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0 搭建测试框架', description='修改HTML报告')
        runner.run(TestBaidu('test_search'))
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='xxx@qq.com',
              server='smtp.163.com',
              sender='xxx@163.com',
              password='',
              path=report
              )
    e.send()
