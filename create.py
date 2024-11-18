from web3 import Web3
from eth_account import Account
import secrets
from mnemonic import Mnemonic

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

def create_eth_wallets(num_wallets):
    w3 = Web3()
    wallets = []
    mnemo = Mnemonic("english")

    for _ in range(num_wallets):
        # Generate mnemonic (seed phrase)
        mnemonic = mnemo.generate(strength=128)  # 12-word mnemonic
        
        # Create account from mnemonic
        acc = Account.from_mnemonic(mnemonic)
        private_key = w3.to_hex(acc._private_key)
        address = acc.address
        
        wallet = {
            'address': address,
            'private_key': private_key,
            'mnemonic': mnemonic
        }
        wallets.append(wallet)

    return wallets

def save_addresses_to_txt(wallets, address_filename='address.txt'):
    with open(address_filename, mode='w') as file:
        for wallet in wallets:
            file.write(f"{wallet['address']}\n")

def save_wallet_data_to_txt(wallets, key_filename='key.txt'):
    with open(key_filename, mode='w') as file:
        file.write("=== Ethereum Wallet Details ===\n")
        for i, wallet in enumerate(wallets, 1):
            file.write(f"=== Wallet #{i} ===\n")
            file.write(f"Address    : {wallet['address']}\n")
            file.write(f"Private Key: {wallet['private_key']}\n")
            file.write(f"Mnemonic   : {wallet['mnemonic']}\n\n")

if __name__ == "__main__":
    print("=== Ethereum Wallet Generator ===\n")
    num_wallets = int(input("Enter the number of wallets to create: "))
    
    try:
        wallets = create_eth_wallets(num_wallets)
        save_addresses_to_txt(wallets)
        save_wallet_data_to_txt(wallets)
        print(f"\nSuccessfully created {num_wallets} wallets!")
        print("- Addresses saved to: address.txt")
        print("- Full details saved to: key.txt")
        print("\nIMPORTANT: Keep your key.txt file secure and backup safely!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")