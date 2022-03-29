import wrap,random
wrap.add_sprite_dir("img_1")
wrap.world.create_world(1350, 500)

import object_physics, mario as mario_mod, dracon,STRELKA
wrap.world.set_back_image("img.png")
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
cloud_platform = wrap.sprite.add("mario-items", 500, 200, "cloud_platform")
cloud_platform2 = wrap.sprite.add("mario-items", 600, 300, "cloud_platform")
cloud_platform3 = wrap.sprite.add("mario-items", 400, 100, "cloud_platform")
grounds_list=[cloud_platform ,cloud_platform2,cloud_platform3,id]
mario = object_physics.create_physics("mario-1-small", mario_mod, 400, 50, "stand", -8,200,grounds_list)
#lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,wrap.sprite.get_top(id))
lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,300,grounds_list)
vode=None
@wrap.on_key_down(wrap.K_1)
def odin():
    global vode
    vode=1


@wrap.on_key_down(wrap.K_2)
def dva():
    global vode
    vode=2

@wrap.always()
def voda():
    if vode == 1:
        STRELKA.ykaz_strelk(mario)
    else:
        STRELKA.ykaz_strelk(lue)


@wrap.always
def run_phisics():
    object_physics.power_gravity(mario)

    object_physics.power_gravity(lue)

@wrap.on_key_down(wrap.K_w)
def jump():
    object_physics.jump(mario)


@wrap.on_key_down(wrap.K_UP)
def jump():

    object_physics.jump(lue)


@wrap.on_key_always(wrap.K_a)
def move():

    object_physics.move_left(mario)




@wrap.on_key_always(wrap.K_d)
def move():
    object_physics.move_right(mario)

@wrap.on_key_always(wrap.K_LEFT)
def move():

    object_physics.move_left(lue)




@wrap.on_key_always(wrap.K_RIGHT)
def move():
    object_physics.move_right(lue)



