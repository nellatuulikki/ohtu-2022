*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nelli
    Set Password  nelli123
    Set Password Confirmation  nelli123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ne
    Set Password  nella123
    Set Password Confirmation  nella123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  nelli
    Set Password  testi1
    Set Password Confirmation  testi1
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  nelli
    Set Password  testisalasana1
    Set Password Confirmation  testisalasana2
    Submit Credentials
    Register Should Fail With Message  Confirmation password doens't match to password

Login After Successful Registration
    Set Username  nelli
    Set Password  testisalasana1
    Set Password Confirmation  testisalasana1
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Login Username  nelli
    Set Login Password  testisalasana1
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  nelli
    Set Password  testisalasana1
    Set Password Confirmation  testisalasana1
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Login Username  nelli
    Set Login Password  testisalasana2
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Ohtu Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  nella  nella123
    Go To Register Page
    Register Page Should Be Open
