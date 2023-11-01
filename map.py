from objects import Block, GoldPad, Fire

def create_map(WIDTH, HEIGHT):
    block_size = 96

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]

    fire = Fire(200, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    objects = [
        *floor,
        Block(block_size * 4, HEIGHT - block_size * 2, block_size),
        GoldPad(block_size * 9, HEIGHT - block_size * 3, block_size),
        fire,
    ]

    return objects, fire
