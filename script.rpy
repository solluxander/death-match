
image ooc = Image("gui/overlay/confirm.png")
image dix = Image("ooc/dix/dix.png") 
image meg = Image("ooc/megan/meg.png")
image sarah = Image("ooc/sarah/sarah.png")
image ex = Image("other/extra.jpeg")

image blorange = Image("blorange/blorange.png")
image twist = Image("twist/twist.png")
image lysander = Image("lysander/lysander.png")


define b = Character("Blorange", image = "blorange") # happy, sad, shock, worry, smug, soft, magic
define c = Character("Clay")
define d = Character("Dix", image = "dix") # happy, sad, shock, worry, smug, sulk, thot, shades, why, ult
define e = Character("Ekene") #1353
define g = Character("Gavenny")
define h = Character("Harriet")
define k = Character("Karina")
define l = Character("Lysander", image = "lysander") #
define m = Character("Megan", image = "meg") # happy, sad, shock, worry, smug, sulk, thot, shades
define n = Character("Nadine") #1614
define o = Character("Olórë")
define p = Character("Pennyfal")
define r = Character("Dice Maiden", what_size=50)
define s = Character("Sarah", image = "sarah") # happy, sad, shock, thot, trauma, why
define t = Character("Twist", image = "twist") # happy, sad, worry, smug, panic, changeling

define bc = Character("Blue Dragonborn")
define br = Character("Brand") #1614
define ki = Character("Ki'on") #
define sh = Character("Shelly")
define te = Character("Teren") #3010

define x = Character("XXX")

init:
  $ rightish = Position(xpos=0.83, ypos=1.0)
  $ leftish = Position(xpos=0.17, ypos=1.0)

  $ far_right = Position(xpos=0.91, ypos=0.75)
  $ mid_right = Position(xpos=0.75, ypos=0.75)
  $ center_right = Position(xpos=0.59, ypos=0.75)
  $ centerish = Position(xpos=0.5, ypos=0.75)
  $ center_left = Position(xpos=0.41, ypos=0.75)
  $ mid_left = Position(xpos=0.25, ypos=0.75)
  $ far_left = Position(xpos=0.09, ypos=0.75)


label start:

  scene ooc

  menu:

    "Welcome to Prison!": 
      jump chap1

    "Lysander, Who Used to be Rich Last Sunday":
      jump chap2

    "So True, Cellmaties! (also blorange fights ki'on)":
      jump chap3

    "channel: twists-death-chat":
      jump chap4

    "Twist and the Terrible, Horrible, No Good, Very Bad Day":
      jump chap5

    "NEXT ->":
      jump men2

  label men2:
  menu:

    "<- PREV":
      jump start

    "Scrying is a Morally and Legally Grey Area ok? ok.":
      jump chap6

    "Twist and the Terrible, Horrible, No Good, Very Bad Day After the Terrible, Horrible, No Good, Very Bad Day":
      jump chap7

    "Intermission and First Arena Battle!!!!!!!!!!!":
      jump chap8

    "I'm a healer AND I'm going to hurt you":
      jump chap9

    "Prison Break!":
      jump chap10


  return
