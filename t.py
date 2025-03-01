import turtle
screen = turtle.Screen()
screen.title("Animación con Turtle")
screen.bgcolor("lightyellow")

linea = turtle.Turtle()
linea.speed(3)
linea.color("black", "blue")
linea.pensize(5)
linea.penup()
linea.goto(200, 0)
linea.pendown()

linea.left(90)
linea.forward(250)
linea.right(110)
linea.forward(250)
linea.right(70)
linea.forward(250)
linea.backward(150)
linea.right(110)
linea.forward(250)
linea.left(110)
linea.forward(150)
linea.left(70)
linea.forward(250)

finish = turtle.Turtle()
finish.speed(2)
finish.color("cyan", "blue")
finish.pensize(5)
finish.penup()
finish.goto(220, 160)
finish.pendown()

finish.left(90)
finish.forward(50)
finish.right(110)
finish.forward(30)
finish.backward(30)
finish.right(70)
finish.forward(20)
finish.left(70)
finish.forward(20)

finish.penup()
finish.goto(260, 150)
finish.pendown()
finish.left(110)
finish.forward(40)

finish.penup()
finish.goto(280, 140)
finish.pendown()
finish.forward(45)
finish.right(150)
finish.forward(60)
finish.left(150)
finish.forward(50)

finish.penup()
finish.goto(330, 120)
finish.pendown()
finish.right(25)
finish.forward(50)
finish.right(140)
finish.forward(55)
finish.backward(30)
finish.right(100)
finish.forward(15)

finish.penup()
finish.goto(380, 100)
finish.pendown()
finish.right(100)
finish.forward(45)
finish.backward(45)
finish.right(100)
finish.forward(30)

tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("blue")
tortuga.turtlesize(2)
tortuga.speed(3)
tortuga.penup()
tortuga.goto(-300, 0)
tortuga.pendown()
tortuga.forward(300)
tortuga.circle(50)  
tortuga.forward(100)
tortuga.circle(50)
tortuga.forward(200)



# Crear tortuga competidora
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("Chocolate4")
t2.penup()
t2.goto(-200, -40)  # Posición inicial
t2.pendown()

# Configurar tortuga para moverse con líneas pequeñas
t2.pensize(2)
t2.speed(5)

t2.begin_fill()  # Inicia el relleno (aunque no se usa una figura cerrada)
for _ in range(25):  # Corrección del bucle
    t2.pendown()
    t2.forward(25)
    t2.penup()
    t2.forward(1)
    
    
t3= turtle.Turtle()
t3.shape("turtle")

t3.color("yellowgreen")
t3.penup()
t3.pensize(2)
t3.goto(-150, -80)  # Posición inicial
t3.pendown()
t3.speed(2)
t3.forward(590)  # Avanza  unidades
t2.end_fill()  # Finaliza el relleno

turtle.done()