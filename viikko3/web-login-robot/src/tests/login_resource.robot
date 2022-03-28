*** Keywords ***

Set Login Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Succeed
    Main Page Should Be Open

Submit Login Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}