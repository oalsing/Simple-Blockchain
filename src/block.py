import datetime
import hashlib


class Block:
    def __init__(self, previous_block_hash, merkle_root, timestamp):
        self.previous_block_hash = previous_block_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.hash = self.get_hash()

    def create_genesis_block(self):
        return Block("0", "0", datetime.datetime.now())

    def create_next_block(self, previous_block):
        prev_block_hash = previous_block.hash
        merkle_root = ""
        timestamp = datetime.datetime.now()

        return Block(prev_block_hash, merkle_root, timestamp)

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) +
                      str(self.merkle_root) +
                      str(self.timestamp))

        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
