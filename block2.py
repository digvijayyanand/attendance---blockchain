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

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 3

    def add_block(self, new_block):
        if len(self.chain) == 0:
            new_block.previous_hash = '0'
        else:
            new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}: {block.timestamp}, Difficulty: {self.difficulty}")

def simulate_pow(num_blocks):
    blockchain = Blockchain()
    for i in range(num_blocks):
        blockchain.add_block(Block(i+1, '', datetime.datetime.now(), {'data': 'Block ' + str(i+1)}))
    return blockchain

if __name__ == "__main__":
    num_blocks = 10
    blockchain = simulate_pow(num_blocks)
    blockchain.print_chain()
