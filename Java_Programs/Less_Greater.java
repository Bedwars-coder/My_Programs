package com.company;
import java.util.Scanner;

public class Less_Greater {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try{
            System.out.println("Enter the first number: ");
            float num1 = sc.nextFloat();
            System.out.println("Enter the second number: ");
            float num2 = sc.nextFloat();

            if (num1 > num2){
                System.out.printf("%f is greater than %f!", num1, num2);
            }
            else if (num1 < num2){
                System.out.printf("%f is less than %f!", num1, num2);
            }
            else{
                System.out.println("The two numbers are equal!");
            }
        }
        catch (Exception error1) {
            System.out.println("Please don't make something go wrong!");
        }
    }
}
