package com.company;
import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        System.out.println("Welcome to advanced calculator!");
        Scanner sc = new Scanner(System.in);
        float a, b, sum, diff, quo, rem, pro;
        char operand;
        System.out.println("Enter your first number");
        a = sc.nextFloat();
        System.out.println("Enter the operand('a' for adding, 's' for subtracting, 'd' for division, 'r' for remainder, 'm' for multiplicationn)");
        operand = sc.next().charAt(0);
        System.out.println("Enter the second number");
        b = sc.nextFloat();
        if (operand == 'a'){
            sum = a + b;
            System.out.println("The sum is " +sum);
        }
        else if (operand == 's'){
            diff = a - b;
            System.out.println("The difference is "+diff);
        }
        else if (operand == 'd'){
            quo = a/b;
            System.out.println("The quotient is "+quo);

        }
        else if (operand == 'r') {
            rem = a % b;
            System.out.println("The remainder is " + rem);

        }
        else if (operand == 'm'){
            pro = a * b;
            System.out.println("The product is "+pro);
        }
        else {
            System.out.println("You need to enter 'a', 's', 'd', 'r', 'm'1");
        }
    }
}
