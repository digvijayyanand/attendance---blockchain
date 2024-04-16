import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_contents = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f'Block {self.index} [Hash: {self.hash}, Previous Hash: {self.previous_hash}, Nonce: {self.nonce}]'

# Let's create a genesis block
def create_genesis_block():
    return Block(0, '0', datetime.datetime.now(), 'Genesis Block')


class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.difficulty = 2

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Create a blockchain instance
blockchain = Blockchain()

# Add some blocks to the blockchain
blockchain.add_block(Block(1, '', datetime.datetime.now(), {'amount': 10}))
blockchain.add_block(Block(2, '', datetime.datetime.now(), {'amount': 20}))
blockchain.add_block(Block(3, '', datetime.datetime.now(), {'amount': 20}))
blockchain.add_block(Block(4, '', datetime.datetime.now(), {'amount': 20}))

# Print the blockchain
blockchain.print_chain()

