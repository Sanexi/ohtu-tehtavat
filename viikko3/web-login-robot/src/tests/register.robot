*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Register Should Succeed

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Register Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Create User  kalle  k
    Register Should Fail With Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    Create User  kalle  kalle123
    Confirm Password  kalle12
    Register Should Fail With Message  Invalid username or password

Login After Successful Registration
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Create User  ka  kalle123
    Go To Login Page
    Login Page Should Be Open
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open