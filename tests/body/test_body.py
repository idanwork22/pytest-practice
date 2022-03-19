from pytest import mark


@mark.body
class BodyTests:

    @mark.ui
    def test_body_system_functions_as_expected(self, chrom_browser):
        chrom_browser.get('https://www.youtube.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
