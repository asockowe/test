import streamlit as st


# import turtle
# import time
# import random
import matplotlib.pyplot as plt
import numpy as np

coll, col2, col3 = st.columns(3)

fig, ax = plt.subplots()
with coll
c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-', '--'])
m1 = st.radio('마커의 형태를 선택하시오', ['o'])
x = []
y = []

for i in range(-20, 21, 2):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)
   


plt.plot(x, y, color=c1, linestyle=s1, marker= 'h')
st.pyplot(fig)
import sys
sys.exit()
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.pensize(5)

# sh = 8
# while True:
#     for i in range(sh):
#         # t.circle(1+5*i)
#         for i in range(4):
#         t.forward(1 + 5*i)
#         t.left(360/sh)
       
#         t.color((random.random(), random.random(), random.random()))
#         t.goto(i*10, 0)   

    



# turtle.done()





    














# for i in range(6):
#     a1 = r.randint(1, 45)
#     a2 = r.random()
#     a1, a2

# a = 0
# for i in range(100):
#     c = r.choice('abcdef')
#     if c == 'a':
#         a = a + 1



# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)

# def square(x, y, lx, ly):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for i in range(4):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)
    

# square(-200, 0, 100, 50)
# square(0, 0, 100, 150)
# square(200, 0, 100, 100)

# turtle.done()

# s = 0
# for i in range(10, 21):
#     s = s + i
# s


# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)

# colors = ['red', 'orange', 'yellow','green', 'blue', 'indigo', 'violet']

# # turtle.bgcolor('black')
# length = 5
# for i in range(50):
#     t.forward(length)
#     # t.pencolor(colors[length%7])
#     t.left(89)
#     length  += 5



# n = 20
# ang = 360/n
# for i in range(n):
#     t.circle(80)
#     t.left(ang)



# turtle.done()


# for i in range(1, 10):
#     if i%3 == 1:
#         i





# '7과 4의 산수 연산'

# '덧셈', 7 + 4
# '뺄셈', 7 - 4
# '곱셈', 7 / 4
# '몫', 7 // 4
# '나머지', 7 % 4
# '거듭제곱', 7 ** 4






# import turtle




# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# # 여기에 코드를 입력



# turtle.done()


# print('hello')
# st.write('hello')
# st.write('강아지'+'고양이')
# st.write('1'+'1')
# st.write(1+2)




# st.write('스트림릿')
# st.title('streamlit image')
#  st.image('1m.jfif')




                                                                                  