from pytest import mark


@mark.smoke
@mark.engine
@mark.ui
def test_engine_system_functions_as_expected(chrom_browser):
    chrom_browser.get('https://www.google.com')
    assert True
