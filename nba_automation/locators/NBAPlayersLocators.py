from selenium.webdriver.common.by import By

class NBAPlayersLocators():

    URL                                  = "https://stats.nba.com/players/traditional/"
    pagination_selector                  = (By.CSS_SELECTOR, ".stats-table-pagination__select")   ##selector
    advance_filter                       = (By.LINK_TEXT,"Advanced Filters")  ## link
    advance_filter_team_byteam           = (By.NAME,"TeamID")  ## selector
    eleventh_row                         = (By.XPATH, "//tr[11]")  ## 
    stats_table                          = (By.CLASS_NAME,"nba-stat-table__overflow")
    run_it                               = (By.CSS_SELECTOR,"a.run-it")
    reset_filters                        = (By.LINK_TEXT,"Reset Filters")