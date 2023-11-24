from blockchain import BlockChain

bc = BlockChain()


bc.mine_block(data="Miniing")
bc.mine_block(data="kingsly")
bc.mine_block(data="james")
bc.mine_block(data="john")
bc.mine_block(data="peter")
bc.get_all_block()