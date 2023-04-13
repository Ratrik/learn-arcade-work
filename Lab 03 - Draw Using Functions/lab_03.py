""" This is a simple picture which was drawn
when I was in a good mood and
Sun was bright and Sky was clear """

import arcade


def draw_sky():
    """ Draw gradient of the sky """
    arcade.draw_lrtb_rectangle_filled(0, 599, 970, 950, (163, 187, 214))
    arcade.draw_lrtb_rectangle_filled(0, 599, 950, 930, (180, 200, 222))
    arcade.draw_lrtb_rectangle_filled(0, 599, 930, 910, (206, 223, 235))
    arcade.draw_lrtb_rectangle_filled(0, 599, 910, 890, (233, 245, 239))
    arcade.draw_lrtb_rectangle_filled(0, 599, 890, 870, (247, 242, 233))
    arcade.draw_lrtb_rectangle_filled(0, 599, 870, 850, (247, 233, 225))
    arcade.draw_lrtb_rectangle_filled(0, 599, 850, 830, (247, 225, 225))
    arcade.draw_lrtb_rectangle_filled(0, 599, 830, 810, (242, 221, 211))
    arcade.draw_lrtb_rectangle_filled(0, 599, 810, 790, (245, 218, 203))
    arcade.draw_lrtb_rectangle_filled(0, 599, 790, 770, (245, 214, 186))
    arcade.draw_lrtb_rectangle_filled(0, 599, 770, 750, (245, 206, 164))
    arcade.draw_lrtb_rectangle_filled(0, 599, 750, 730, (245, 204, 152))
    arcade.draw_lrtb_rectangle_filled(0, 599, 730, 710, (245, 198, 140))
    arcade.draw_lrtb_rectangle_filled(0, 599, 710, 690, (242, 189, 124))
    arcade.draw_lrtb_rectangle_filled(0, 599, 690, 670, (237, 180, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 670, 650, (237, 173, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 650, 630, (237, 162, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 630, 610, (237, 147, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 610, 590, (237, 132, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 590, 570, (237, 117, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 570, 550, (237, 102, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 550, 530, (237, 87, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 530, 510, (237, 72, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 510, 490, (237, 57, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 490, 470, (237, 42, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 470, 450, (237, 27, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 450, 430, (237, 12, 109))
    arcade.draw_lrtb_rectangle_filled(0, 599, 430, 410, (237, 12, 85))


def drawing_mountains():
    """ Drawing mountains """
    arcade.draw_lrtb_rectangle_filled(0, 599, 380, 0, (151, 162, 186))
    arcade.draw_polygon_filled(((150, 420), (160, 413), (170, 410), (180, 412),
                                (190, 413), (200, 415), (210, 417), (220, 420), (230, 418), (240, 415), (250, 413),
                                (260, 416),
                                (270, 417), (280, 420), (290, 421), (300, 424), (310, 417), (320, 420), (330, 418),
                                (340, 417), (350, 414), (360, 412), (370, 410), (380, 412), (390, 411), (400, 414),
                                (410, 417), (420, 420), (430, 419), (440, 417), (450, 415), (460, 416), (470, 417),
                                (480, 421), (490, 423), (500, 424), (510, 419), (520, 420), (530, 418), (540, 416),
                                (550, 411), (560, 414), (570, 417), (580, 418), (599, 421), (599, 380), (150, 380)),
                               (151, 162, 186))
    arcade.draw_polygon_filled(((120, 435), (130, 431), (140, 423), (150, 420), (160, 413), (170, 400), (180, 398),
                                (190, 393), (200, 390), (210, 385),
                                (220, 383), (230, 380), (240, 378), (250, 376), (260, 373), (270, 370), (280, 369),
                                (290, 367), (300, 363), (310, 365), (320, 366), (330, 362), (340, 360), (350, 357),
                                (360, 353), (370, 357), (380, 350), (390, 348), (400, 345), (410, 346),
                                (420, 343), (430, 348), (440, 350), (450, 356), (460, 353), (470, 357), (480, 360),
                                (490, 363), (500, 367), (510, 369), (520, 373), (530, 372), (540, 375), (550, 377),
                                (560, 373), (570, 371), (580, 370), (599, 368), (599, 320), (150, 320)),
                               (109, 123, 153))
    arcade.draw_polygon_filled(((270, 320), (280, 325), (290, 327), (300, 331), (310, 335), (320, 341), (330, 348),
                                (340, 356), (350, 360), (360, 369), (370, 377), (380, 389), (390, 394), (400, 399),
                                (410, 405), (420, 408), (430, 410), (440, 407), (450, 400), (460, 393), (470, 382),
                                (480, 380), (490, 376), (500, 371), (510, 362), (520, 353), (530, 350), (540, 348),
                                (550, 337), (560, 333), (570, 331), (580, 330), (599, 328), (599, 250), (270, 250)),
                               (74, 88, 117))
    arcade.draw_polygon_filled(((170, 350), (180, 348), (190, 343), (200, 340), (210, 335),
                                (220, 333), (230, 330), (240, 328), (250, 326), (260, 323), (270, 320), (280, 319),
                                (290, 317), (300, 313), (310, 315), (320, 316), (330, 312), (340, 310), (350, 307),
                                (360, 303), (370, 297), (380, 290), (390, 288), (400, 285), (410, 286),
                                (420, 283), (430, 278), (440, 276), (450, 273), (460, 275), (470, 277), (480, 273),
                                (490, 270), (500, 267), (510, 269), (520, 267), (530, 266), (540, 264), (550, 267),
                                (560, 263), (570, 261), (580, 260), (599, 258), (599, 220), (170, 220)),
                               (56, 72, 105))
    arcade.draw_polygon_filled(((0, 500), (10, 498), (20, 495), (30, 493), (40, 490), (50, 488), (60, 486),
                                (70, 473), (80, 460), (90, 459), (100, 447), (110, 443), (120, 435), (130, 426),
                                (140, 412), (150, 400), (160, 387), (170, 375), (180, 357), (190, 340),
                                (200, 328), (210, 325), (220, 315), (230, 310), (240, 308), (250, 296),
                                (260, 283), (270, 280), (280, 269), (290, 257), (300, 253), (310, 245),
                                (320, 236), (330, 222), (340, 210), (340, 0), (0, 0)),
                               (25, 38, 64))
    arcade.draw_polygon_filled(((200, 0), (210, 30),
                                (220, 50), (230, 70), (240, 100), (250, 120), (260, 150), (270, 180), (280, 230),
                                (290, 250), (300, 270), (310, 285), (320, 300), (330, 303), (340, 308), (350, 307),
                                (360, 310), (370, 316), (380, 312), (390, 318), (400, 320), (410, 325),
                                (420, 331), (430, 334), (440, 338), (450, 341), (460, 345), (470, 344), (480, 346),
                                (490, 347), (500, 349), (510, 353), (520, 355), (530, 357), (540, 358), (550, 360),
                                (560, 363), (570, 361), (580, 360), (599, 365), (599, 0), (200, 0)),
                               (3, 17, 46))


def draw_cloud(x):
    arcade.draw_circle_filled(x + 10, 605, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 30, 610, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 50, 613, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 70, 615, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 90, 610, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 110, 607, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 130, 605, 20, (245, 232, 213))
    arcade.draw_circle_filled(x + 10, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 30, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 50, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 70, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 90, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 110, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x + 130, 600, 20, (250, 225, 212))
    arcade.draw_circle_filled(x, 600, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 10, 595, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 30, 590, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 50, 587, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 70, 585, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 90, 590, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 110, 592, 20, (247, 220, 203))
    arcade.draw_circle_filled(x + 130, 597, 20, (247, 220, 203))


def draw_picture(delta_time):
    """ Draw picture """
    arcade.start_render()
    draw_sky()
    drawing_mountains()
    draw_cloud(draw_picture.x)

    draw_picture.x += 1


draw_picture.x = -160


def main():
    arcade.open_window(600, 1000, 'Simple picture')
    arcade.set_background_color((150, 176, 212))

    arcade.schedule(draw_picture, 1/60)
    arcade.run()


# Call the main function to get the program started
main()
