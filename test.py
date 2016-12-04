from carrom import Pocket, BaseCoin

positions = [('red', 'r1', 496.8056422489117, 497.53927172225013), ('white', 'w1', 473.1673948908587, 479.3298824669012), ('white', 'w2', 464.2231931878116, 472.4398432892017), ('white', 'w3', 535.7768068121884, 527.5601567107983), ('white', 'w4', 504.108325050695, 531.6684817614935), ('white', 'w5', 531.6684817614935, 495.891674949305), ('white', 'w6', 545.4485601168926, 478.0032715432108), ('white', 'w7', 500.7275516016571, 443.55307565471276), ('white', 'w8', 490.3282466952958, 549.5568851675877), ('white', 'w9', 454.5514398831074, 521.9967284567892), ('black', 'b1', 517.8884034060942, 513.7800783553992), ('black', 'b2', 468.3315182385066, 504.108325050695), ('black', 'b3', 459.3873165354595, 497.2182858729955), ('black', 'b4', 513.0525267537421, 538.558520939193), ('black', 'b5', 495.891674949305, 468.3315182385066), ('black', 'b6', 486.9474732462579, 461.441479060807), ('black', 'b7', 549.5568851675877, 509.6717533047041), ('black', 'b8', 536.5043584138455, 471.1132323655112), ('black', 'b9', 481.3840449922487, 542.666845989888)]


pocket = Pocket((967.7419 , 32.2581))
for p in positions:
    coin = BaseCoin(p[0], p[1], (p[2], p[3]))
    coin.target_to_pocket(pocket)
