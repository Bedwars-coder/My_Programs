package com.company;

import java.util.Scanner;

public class Factorial_calc {
    public static int calcFactOf(int boundTo) {
        if (boundTo == 0) {
            return 0;
        }
        else if (boundTo == 1) {
            return 1;
        }
        else {
            int result = 1;
            result = boundTo * calcFactOf(boundTo - 1);
            return result;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number whose factorial you want to calculate: ");
        int number = sc.nextInt();
        System.out.println("The factorial is " +calcFactOf(number));
    }
}
