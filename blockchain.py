import datetime as _dt
import hashlib as _hash
import json as _json

class BlockChain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self.create_block(index=0, proof_of_work=1, previous_hash="0", data="Genesis Block")
        self.chain.append(genesis_block)
    
    def create_block(self, index: int,proof_of_work: int, previous_hash:str, data: str) -> dict:
         block = {
             "index": index,
             "data": data,
             "time_stamp": str(_dt.datetime.now()),
             "proof_of_work": proof_of_work,
             "previous_hash": previous_hash

        }
         
         return block
    


        