#!/bin/bash

i=1
ii=20
iii=2
sum=0
num=50
school1="corpus"
school2="kingsville"
school3="commerce"
<<com
while [ $i -le 15 ]
do
        echo $i
        let i++
done

until [ ! $i -le 15 ]
do
        echo $i
        let i++
done

for i in $(seq 1 1 15)
do
        echo $i
done


while [ $ii -le 40 ]
do
        sum=$((sum + ii))
        let ii++
done

echo $sum


until [ ! $ii -le 40 ]
do
        sum=$((sum + ii))
        let ii++
done

echo $sum


for ii in $(seq 20 1 40)
do
        sum=$((sum + ii))
        let ii++
done

echo $sum
com



















echo "what A&M school are you attending:corpus,kingsville,commerce,college station"
read school
if [ "$school" == "$school1" ]
then
        echo "you are attending Texas A&M University Corpus Christi"
elif [ "$school" == "$school2" ]
then
        echo "you are attending Texas A&M University Kingsville"
elif [ "$school" == "$school3" ]
then
        echo "you are attending Texas A&M University Commerce"
else
        echo "you are attending Texas A&M University"
fi
