class Block:
    def __init__(self, block_hash, previous_block_hash, data) -> None:
        self.index = 1
        self.block_hash =block_hash
        self.previous_block_hash = previous_block_hash
        self.data = data

class BlockChain:
    def __init__(self) -> None:
        self.chain = list()