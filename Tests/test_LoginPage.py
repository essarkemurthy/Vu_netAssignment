import pytest
from Pages.LoginPage import LoginPage
from Pages.ResultsPage import ResultsPage
from Tests.test_Base import BaseTest
from utilities.ReadExcel import ReadExcelData


class Test_Login(BaseTest):
    data = ReadExcelData(file_location="../testData/testdata_sites.xlsx", sheet_name="Websites").get_data()
    print(len(data))

    @pytest.mark.parametrize('arg1', data)
    def test_login(self, arg1):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(arg1['Site URL'], arg1['email'])
        self.results_page = ResultsPage(self.driver)
        scores = self.results_page.get_results()
        final_result = self.results_page.validate_score(scores)
        assert final_result
