from objects import Fire, Block, GrassBlock, IceBlock, GoldPad, WoodPad, XGoldBorder, YGoldBorder, SwampMiniBlock

def create_map(WIDTH, HEIGHT):
    block_size = 96

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

    fire = Fire(200, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    objects = [
        *floor,

        GoldPad(block_size * 6, HEIGHT - block_size * 2, block_size),
        WoodPad(block_size * 7, HEIGHT - block_size * 2, block_size),

        Block(block_size * 8, HEIGHT - block_size * 3, block_size),
        GrassBlock(block_size * 9, HEIGHT - block_size * 3, block_size),

        IceBlock(block_size * 11, HEIGHT - block_size * 2, block_size),
        SwampMiniBlock(block_size * 12, HEIGHT - block_size * 1.62, block_size),

        XGoldBorder(block_size * 14, HEIGHT - block_size * 2, block_size),
        YGoldBorder(block_size * 15.5, HEIGHT - block_size * 2, block_size),
        
        fire,
    ]

    return objects, fire
