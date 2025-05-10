import hashlib
import random
import string
import time

class HashingDemo:
    def __init__(self):
        # Simple hash table to store username -> hashed password
        self.user_database = {}
        
        # Dictionary to store salts
        self.salt_storage = {}
        
        # Array to demonstrate collision handling (for simple hash function)
        self.collision_demo = [None] * 10
    
    def simple_hash(self, text):
        """
        A very simple hash function for demonstration
        (NOT cryptographically secure - just for education)
        """
        hash_value = 0
        for char in text:
            hash_value += ord(char)
        return hash_value % 10
    
    def generate_salt(self, length=8):
        """Generate a random salt"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    def demonstrate_hashing_techniques(self, username, password):
        """Show different hashing techniques"""
        print(f"\n=== Demonstrating Password Hashing for '{username}' ===")
        print(f"Original password: {password}")
        print("-" * 50)
        
        # 1. Simple hash (insecure - for demonstration)
        simple_hash_value = self.simple_hash(password)
        print(f"1. Simple Hash Function (educational only):")
        print(f"   Hash value: {simple_hash_value}")
        print(f"   Array index: {simple_hash_value}")
        print(f"   Problem: Collisions and not secure!")
        print()
        
        # 2. MD5 (deprecated but educational)
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        print(f"2. MD5 Hash (deprecated - don't use in production):")
        print(f"   Hash: {md5_hash}")
        print(f"   Length: {len(md5_hash)} characters")
        print(f"   Problem: Vulnerable to rainbow tables")
        print()
        
        # 3. SHA-256 without salt
        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        print(f"3. SHA-256 Hash (better but needs salt):")
        print(f"   Hash: {sha256_hash}")
        print(f"   Length: {len(sha256_hash)} characters")
        print(f"   Problem: Still vulnerable to rainbow tables")
        print()
        
        # 4. SHA-256 with salt (recommended)
        salt = self.generate_salt()
        salted_password = salt + password
        sha256_salted = hashlib.sha256(salted_password.encode()).hexdigest()
        print(f"4. SHA-256 with Salt (recommended):")
        print(f"   Salt: {salt}")
        print(f"   Salted password: {salted_password}")
        print(f"   Hash: {sha256_salted}")
        print(f"   Benefit: Each user has unique hash even with same password")
        print()
        
        # Store the salted hash (this is what we'd actually use)
        self.salt_storage[username] = salt
        self.user_database[username] = sha256_salted
        
        # 5. Show how the same password with different salts produces different hashes
        salt2 = self.generate_salt()
        salted_password2 = salt2 + password
        sha256_salted2 = hashlib.sha256(salted_password2.encode()).hexdigest()
        print(f"5. Same Password with Different Salt:")
        print(f"   New salt: {salt2}")
        print(f"   New hash: {sha256_salted2}")
        print(f"   Notice: Completely different hash for same password!")
        print()
        
        return sha256_salted
    
    def verify_password(self, username, password):
        """Demonstrate password verification"""
        if username not in self.user_database:
            return False, "User not found"
        
        # Get the stored salt
        salt = self.salt_storage[username]
        
        # Hash the provided password with the same salt
        salted_password = salt + password
        hash_to_check = hashlib.sha256(salted_password.encode()).hexdigest()
        
        # Compare with stored hash
        stored_hash = self.user_database[username]
        
        print(f"\n=== Password Verification Process ===")
        print(f"Username: {username}")
        print(f"Stored salt: {salt}")
        print(f"Input password: {password}")
        print(f"Input + salt: {salted_password}")
        print(f"Generated hash: {hash_to_check}")
        print(f"Stored hash:    {stored_hash}")
        print(f"Match: {hash_to_check == stored_hash}")
        
        return hash_to_check == stored_hash, "Password verified" if hash_to_check == stored_hash else "Invalid password"

def main():
    demo = HashingDemo()
    
    while True:
        print("\n=== Password Hashing Demonstration ===")
        print("1. Create user and demonstrate hashing techniques")
        print("2. Verify password (login simulation)")
        print("3. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            demo.demonstrate_hashing_techniques(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = demo.verify_password(username, password)
            print(f"\nResult: {message}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()