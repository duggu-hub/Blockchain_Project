#The goal of this project is to create a simple blockchain in Python that allows us to add blocks containing transactions to a chain.
#This serves as a foundational introduction to the concepts of blockchain technology, including hashing, block creation, and the structure of a blockchain.
  
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}".encode('utf-8')
    return hashlib.sha256(value).hexdigest()
  
def create_genesis_block():
    timestamp = time.time()
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))
  
def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    previous_hash = previous_block.hash
    new_hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, new_hash)

blockchain = [create_genesis_block()]

def add_block(data):
    previous_block = blockchain[-1]
    new_block = create_new_block(previous_block, data)
    blockchain.append(new_block)

add_block("First block after Genesis")
add_block("Second block after Genesis")

# Display the blockchain
for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}\n")
