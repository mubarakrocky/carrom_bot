from carrom import Pocket, BaseCoin
pocket = Pocket((900, 0))
coin = BaseCoin("black", 1, (100,0))
coin.target_to_pocket(pocket)
