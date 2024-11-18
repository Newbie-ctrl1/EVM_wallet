
# Ethereum Wallet Generator

## Description

Ethereum Wallet Generator is a Python script that allows you to create multiple Ethereum wallets, including details such as the address, private key, and mnemonic (seed phrase). The generated wallets will be saved into two separate files:

- `address.txt`: Contains a list of Ethereum wallet addresses.
- `key.txt`: Contains full wallet details (address, private key, and mnemonic).

## Features

- **Automatically generates Ethereum wallets using HD Wallet functionality.**
- **Saves wallet addresses to `address.txt`.**
- **Saves private key, mnemonic, and address to `key.txt` for each wallet created.**
- **Utilizes the Web3, eth_account, and mnemonic libraries.**

## Requirements

Make sure you have installed the required dependencies before running the script. You can use pip to install the necessary packages.

## Installation
1. Ensure that Python 3 is installed on your system.
2. Install the required dependencies by running the following command:
  ```bash
  pip install web3 eth-account mnemonic
  ```

## Usage

1. Run the script using Python:
  ```bash
  python wallet_generator.py
  ```
2. Once the script starts, you will be prompted to enter the number of wallets you want to create. Input the desired number.
3. After generating the wallets, the information will be saved into two files:
    - `address.txt`: Only contains the wallet addresses.
    - `key.txt`: Contains the address, private key, and mnemonic for each generated wallet.
4. Important: Make sure to securely store the `key.txt` file, as it contains sensitive information like private keys and mnemonics that can be used to access your wallets.

## utput Files
- **`address.txt`: This file stores wallet addresses in plain text, one address per line.**

  Example of address.txt:
  ```
  0x1234567890abcdef1234567890abcdef12345678
  0xabcdef1234567890abcdef1234567890abcdef12
  ```
- **`key.txt`: This file stores full details of each wallet, including the address, private key, and mnemonic (seed phrase) for recovery.**

  Example of key.txt:
   ``` yaml
    === Ethereum Wallet Details ===

    === Wallet #1 ===
    Address    : 0x1234567890abcdef1234567890abcdef12345678
    Private Key: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
    Mnemonic   : legal winner thank year wave sausage worth useful legal winner thank yellow

    === Wallet #2 ===
    Address    : 0xabcdef1234567890abcdef1234567890abcdef12
    Private Key: 0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
    Mnemonic   : moon bridge razor bean cry illegal flat winner fork trust yellow question
  ```
   
## Warning

Private Key and Mnemonic are highly sensitive information. Never share the key.txt file with anyone and ensure it is backed up securely.
Anyone with access to the private key or mnemonic can control the assets in your Ethereum wallet.
## License

This project is licensed under the MIT License. See the LICENSE file for more details.
