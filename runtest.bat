set BROWSER=chrome
::set ROBOT_SYSLOG_FILE=rflog.txt
::set PROJECT_URL=https://beryllium.dev.yellow.co.nz
::set PROJECT_URL=https://beryllium.qa.yellow.co.nz
::set PROJECT_URL=https://yellow.co.nz
set PROJECT_URL=https://beryllium.staging.yellow.co.nz
set outputdir=C:\Test Automation\Beryllium2\beryllium_regression_test\
set Testlink_Tag=T
set Jenkins_Build_ID=1

DEL "C:\Test Automation\Beryllium2\beryllium_regression_test\*.png"
:: robot --exclude need_captcha pages\details_listing_page.robot pages\flybuys.robot pages\home_page.robot pages\login_page.robot pages\search_results_page.robot pages\yellowmove.robot
:: robot --include YOL-258-4 --exclude need_captcha review registration_login pages search
:: robot --include YOL-258-21 --include debug review\manage_reviews.robot
:: robot beryllium_regression_test/pages/consumer_home_page.robot
:: robot --exclude skip_qa */consumer_home_page.robot
::robot  --include date_reviews  pages/new_detailed_listing_page.robot
::robot        */new_detailed_listing_page.robot
::robot        */online_profile_page.robot
robot    login/login.robot
cmd.exe
