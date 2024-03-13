import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("TÜRK BAYRAĞI")
w.setup(width=720,height=420)
w.bgcolor("red")

# İlk daire
t.up()
t.goto(-100,-100)
t.color('white')
t.begin_fill()
t.circle(120)
t.end_fill()

# Hilal yapabilmek için ikinci daire
t.goto(-70,-80)
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

# Yıldız için hazırlık
t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

# Yıldız için tekrar eden üçgen çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# Yıldızın içini doldurmak için tekrar bir daire çizimi
t.goto(75,-20)
t.color('white')
t.begin_fill()
t.circle(30)
t.end_fill()

# Fare imleci ekranda durup görüntüyü bozmasın diye uzaklaştırıyoruz :)
t.goto(-999,-0)

# Ekrana tıklayınca programın kapanmasını sağlar.
w.exitonclick()
