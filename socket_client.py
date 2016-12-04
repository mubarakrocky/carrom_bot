from socketIO_client import SocketIO, BaseNamespace

class Message(BaseNamespace):
    
    def on_connect_game(self, *args):
        print('connect_game', args)
        
    def on_connect(self):
        print('[Connected]')
        
    def on_your_turn(self, *args):
        self.player.coins_factory(args[0]['position'])
        self.player.process(self)
        
    def on_player_input(self, *args):
        print('player_input', args)
        
    def set_player(self, player):
        self.player = player
        

def start(player, game_key, player_key):
    socketIO = SocketIO('localhost', 4000, Message)
    socketIO.get_namespace().set_player(player)
    socketIO.emit('connect_game', {'playerKey': player_key, 'gameKey': game_key})
    socketIO.wait()