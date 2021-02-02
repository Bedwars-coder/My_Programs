package com.company;

import java.util.Scanner;

public class star_Pattern {
    public static void main(String[] args) {
        // A simple Java program to print a star pattern using for loops!
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1 or 0:");
        int one_or_zero = sc.nextInt();
        System.out.println("Enter the number of rows you want: ");
        int rows = sc.nextInt();
        switch (one_or_zero){
            case 1 -> {
               for (int i = 0; i <= rows; i++){
                   for (int j = 1; j <= i; j++){
                       System.out.print("*");
                   }
                   System.out.println();
               }
            }
            case 0 -> {
                for (int i = rows; i > 0; i--){
                    for (int j = 1; j <= i; j++){
                        System.out.print("*");
                    }
                    System.out.println();
                }
            }
            default -> System.out.println("You did not enter 0 or 1!");
        }
    }
}
