package main

import (
	"fmt"
	"math"
)

type Color struct {
	color string
}
type Figure interface {
	Area() float64
}

type Rectangle struct {
	width  float64
	length float64
	color  Color
}

type Square struct {
	side  float64
	color Color
}

type Circle struct {
	radius float64
	color  Color
}

func NewColor(color string) Color {
	return Color{color: color}
}
func NewRectangle(width, length float64, color string) Rectangle {
	return Rectangle{width: width, length: length, color: NewColor(color)}
}
func (r Rectangle) Area() float64 {
	return r.width * r.length
}

func (r Rectangle) String() string {
	return fmt.Sprintf("Прямоугольник %s цвета с длиной стороны %v, шириной стороны %v, площадью %v.",
		r.color.color, r.length, r.width, r.Area())
}

func NewSquare(side float64, color string) Square {
	return Square{side: side, color: NewColor(color)}
}

func (s Square) Area() float64 {
	return s.side * s.side
}

func (s Square) String() string {
	return fmt.Sprintf("Квадрат %s цвета с длиной стороны %v, площадью %v.",
		s.color.color, s.side, s.Area())
}

func NewCircle(radius float64, color string) Circle {
	return Circle{radius: radius, color: NewColor(color)}
}

func (c Circle) Area() float64 {
	return math.Pi * (c.radius * c.radius)
}

func (c Circle) String() string {
	return fmt.Sprintf("Круг %s цвета радиусом %v, площадью %v.",
		c.color.color, c.radius, c.Area())
}

func main() {
	r := NewRectangle(5, 5, "синего")
	c := NewCircle(5, "зеленого")
	s := NewSquare(5, "красного")

	fmt.Println(r)
	fmt.Println(c)
	fmt.Println(s)
}
