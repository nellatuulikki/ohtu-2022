*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nelli  nella123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  nella  nella123
    Output Should Contain  Username is taken

Register With Too Short Username And Valid Password
    Input Credentials  ne  nella123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  neltsu  testi1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  neltsut  testataansalasanaa
    Output Should Contain  Invalid password

*** Keywords ***
Create User And Input New Command
    Create User  nella  nella123
    Input New Command