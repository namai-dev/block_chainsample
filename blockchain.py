import datetime as _dt
import hashlib as _hash
import json as _json

class BlockChain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self.create_block(index=0, proof_of_work=1, previous_hash="0", data="Genesis Block")
        self.chain.append(genesis_block)
    
    def mine_block(self, data:str):
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof_of_work"]
        index = len(self.chain)+1
        proof = self._proof_of_work(data=data, previous_proof=previous_proof, index=index)
        previous_hash = self._hash_block(block=previous_block)
        block = self.create_block(index=index, previous_hash=previous_hash,  proof_of_work=proof, data=data)
        self.chain.append(block)
        return block
    


    def _hash_block(self, block: dict):
        encoded_block = _json.dumps(block, sort_keys=True).encode()
        return _hash.sha256(encoded_block).hexdigest()

    def _to_digest(self,new_proof:int, previous_proof: int, index: int, data: str) -> bytes:
        to_digest =str(new_proof **2 - previous_proof **2 + index) + data
        return to_digest.encode()
    




    def _proof_of_work(self, previous_proof: int, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            print(new_proof)
            to_digest = self._to_digest(new_proof=new_proof, previous_proof=previous_proof, index=index, data=data)
            hash_value = _hash.sha256(to_digest).hexdigest()
            print(hash_value)
            if hash_value[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    

    
    def get_previous_block(self):
        return self.chain[-1]
    
    def create_block(self, index: int,proof_of_work: int, previous_hash:str, data: str) -> dict:
         block = {
             "index": index,
             "data": data,
             "time_stamp": str(_dt.datetime.now()),
             "proof_of_work": proof_of_work,
             "previous_hash": previous_hash

        }
         
         return block
    
    def get_all_block(self):
        for chain in self.chain:
            print(chain)
        
    


        