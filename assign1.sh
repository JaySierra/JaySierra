#!/bin/bash
echo "this is assignment 7"

name="Jay Sierra"
courses="math,english,scripts,seminar,cocs"
echo "my name is $name"
echo "the courses i take are $courses"

echo "$@"
echo "$$"

echo "enter a number between 1-100"
read number
if [[ $number -le 100 && $number -ge 90 ]]
then
        echo "you got an A"
elif [[ $number -le 89 && $number -ge 80 ]]
then
        echo "you got an B"
elif [[ $number -le 79 && $number -ge 70 ]]
then
        echo "you got an C"
elif [ $number -le 69 ]
then
        echo "you failed"
else
        echo "something went wrong"
fi

number1=15
number2=10
sum=0
echo "numbers are $number1 and $number2"

echo "addition"
sum=$((number1+number2))
echo "$sum"

echo "subtraction"
sum=$((number1-number2))
echo "$sum"

echo "division"
sum=$((number1/number2))
echo "$sum"

echo "multiplication"
sum=$((number1*number2))
echo "$sum"

echo "increment"
echo $((++number1))
echo "$number1"

echo "decrement"
echo $((--number2))
echo "$number2"
