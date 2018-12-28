from selenium.webdriver.common.by import By

class NBALeadersLocators():


    URL                                = "http://stats.nba.com/leaders/"
    player_leader_table                = (By.CLASS_NAME,"nba-stat-table__overflow")
    pagination_selector                = (By.CSS_SELECTOR, ".stats-table-pagination__select")   ##selector
    eleventh_row                       = (By.XPATH, "//tr[11]")


class NBAPlayerPage():

    player_name                         = (By.CLASS_NAME, "player-summary__player-name")
    player_stats_div                    = (By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div/div/div/div[2]/div[1] ")
    