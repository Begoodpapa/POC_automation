*** Settings ***
Documentation
...                 Steps definition are defined in this file.
...                 For operation-related keywords, add them to helper.robot
...                 General rule of thumb is that domain or business-specific keywords
...                 should go here.
Library             Selenium2Library    30
Library             Dialogs
Library             DateTime
Resource            helper.robot


*** Keywords ***
Go to home page
    Go To Url And Wait For Element    ${TEST_URL}    ${navloginpanel_navlogin}

Go to consumer main page
    Go To Url And Wait For Element    ${TEST_URL}${url_consumer_main_page}    ${home_consumer_tab_find_a_business_section}

Wait until modal backdrop to be faded
    : FOR    ${i}    IN RANGE    1    5
    \   ${status}=    Run keyword and return status    Element should be visible    ${login_modal_backdrop}
    \   Run keyword if    ${status}    sleep    1s
    \   Run keyword unless    ${status}    exit for loop

Logout
    Select Window    main
    Click Element And Wait For Another Element    ${my_navlogin_dropdown_arrow}    ${my_navloginpanel_signout}
    Click Element    ${my_navloginpanel_signout}

