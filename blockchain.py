import datetime as _dt
import hashlib as _hash
import json as _json

class BlockChain:
    def __init__(self) -> None:
        self.chain = list()
        self.block = None
    
    def create_block(self, index: int,proof_of_work: int, previous_hash:str, data: str) -> dict:
         block = {
             "index": index,
             "data": data,
             "time_stamp": str(_dt.datetime.now()),
             "proof_of_work": proof_of_work,
             "previous_hash": previous_hash

        }
         
         return block

        