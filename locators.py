from selenium.webdriver.common.by import By


class BasePageLocators:
    ELEMENTS = (By.CSS_SELECTOR, ".category-cards > :nth-child(1)")
    check_box = (By.CSS_SELECTOR, ".accordion > :nth-child(1)  #item-1")
    open_home = (By.CSS_SELECTOR, ".rct-text > :nth-child(1)")
    open_downloads = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > button")
    check_box_file =  (By.CSS_SELECTOR,"#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    text1 = (By.CSS_SELECTOR,"#result :nth-child(1)")
    text2 = (By.CSS_SELECTOR,"#result :nth-child(2)")


