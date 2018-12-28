from selenium.webdriver.common.by import By

class NBAStandingsLocators():

    URL                          = "https://stats.nba.com/standings/"
    FILTER_SEASONTYPE            = (By.NAME, 'Season')
    FILTER_GROUPBY               = (By.NAME, 'GroupBy')
    CONF_TABLES                  = (By.TAG_NAME, 'nba-stat-table')