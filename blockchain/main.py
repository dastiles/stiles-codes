import hashlib


class NeuralCoinBlock:
    def __init__(self, previous_blocks_hash, transaction_list):
        self.previous_blocks_hash = previous_blocks_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + \
            "-" + previous_blocks_hash
        self.block_hash = hashlib.sha3_256(
            self.block_data.encode()).hexdigest()


t1 = "Ann sends 2 NC to Mike"
t2 = "Bob sends 5.2 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 0.3 NC to Ann"
t5 = "Mike sends 1 NC to charlie"
t6 = "Mike sends 5.4 NC to Mike"


initial_block = NeuralCoinBlock('initial String', [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)
