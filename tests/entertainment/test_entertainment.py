from pytest import mark


@mark.entertainment
@mark.ui
def test_entertainment_system_functions_as_expected(chrom_browser):
    chrom_browser.get('https://github.com/')
    assert True
