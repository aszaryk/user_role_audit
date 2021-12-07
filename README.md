# Output list of API users and IP address restrictions

Script to output Veracode users and associated IP login restrictions assigned

Uses Python3

## Setup

Clone this repository:

    git clone https://github.com/aszaryk/user_role_audit

Install dependencies:

    cd user_role_audit
    pip3 install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## Usage

Tested using Python3 

usage: Get_All_User_Info.py



## Run

If you have saved credentials as above you can run:

    python3 Get_All_User_Info.py
    
Otherwise you will need to set environment variables before running `Get_All_User_Info.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python3 Get_All_User_Info.py
