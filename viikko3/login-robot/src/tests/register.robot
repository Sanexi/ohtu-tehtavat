*** Settings ***
Resource  resource.robot
Library  ../AppLibrary.py

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle12  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  error

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  error

Register With Valid Username And Too Short Password
    Input Credentials  kalle  ka
    Output Should Contain  error

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalleeee
    Output Should Contain  error