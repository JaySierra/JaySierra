#!/bin/bash

filen="filee.txt"
sum=0
filenmae="numbers11.txt"
summation (){
        while read line
        do
                echo $line
                let sum+=$line
        done < $filenmae
echo $sum
}
summation $filename

echo "enter in number"
read n
a=0
b=1
fib (){
        for (( i=0; i<n; i++ ))
        do
                echo -n " $a "
                fn=$((a + b))
                a=$b
                b=$fn
        done
}
fib $n

echo $sum >> $filen
echo $fn >> $filen



numbers=(5 4 8 9 2 3 7 1)
sorting (){
        sort=0
        echo ${numbers[@]}
        lens=${#numbers[@]}

        for((i=0; i<$lens; i++))
        do
                for((j=i+1; j<$lens; j++))
                do
                        if [ ${numbers[i]} -gt ${numbers[j]} ]
                        then
                                continue
                        else
                                sort=${numbers[i]}
                                numbers[i]=${numbers[j]}
                                numbers[j]=$sort
                        fi
                done
        done
        echo ${numbers[@]}
}
sorting $numbers
