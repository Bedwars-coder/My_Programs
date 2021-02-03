package com.company;

import java.util.Scanner;

public class star_Pattern_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i = 0;
        System.out.println("Enter 0 or 1:");
        int zero_or_one = sc.nextInt();
        System.out.println("Enter the number of rows you want:");
        int rows = sc.nextInt();
        String star = "*";

        switch (zero_or_one) {
            case 0 -> {
                while (i <= rows) {
                    System.out.println(star.repeat(i));
                    i++;
                }
            }
            case 1 -> {
                while (rows > 0){
                    System.out.println(star.repeat(rows));
                    rows--;
                }
            }
            default -> System.out.println("You need to enter 0 or 1. Kindly enter 1 or 0!");
        }
    }
}
