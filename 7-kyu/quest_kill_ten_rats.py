def world_quest():
    world = World()
    world.talk("npc", "hi")
    world.talk("npc", "Alper")
    world.talk("npc", "yes")
    killed = 0

    while killed < 10:
        world.pickup("rock")
        if world.throw("rat"):
            killed += 1

    world.talk("npc", "hello")
    return world
