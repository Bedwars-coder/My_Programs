package com.company;

import java.util.Scanner;

public class star_Pattern_3 {
    public static void main(String[] args) {
        // Printing star pattern using do...while loops!
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter the number of rows you want:");
            int rows = sc.nextInt();
            System.out.println("Enter 0 or 1:");
            int one_or_zero = sc.nextInt();
            String star = "*";
            int c = 0;
            switch (one_or_zero) {
                case 0 -> {
                    do {
                        System.out.println(star.repeat(c));
                        c++;
                    } while (c <= rows);
                }
                case 1 -> {
                    do {
                        System.out.println(star.repeat(rows));
                        rows--;
                    } while (rows > 0);
                }
                default -> System.out.println("You need to enter 0 or 1!");
            }
        } catch (Exception error1) {
            System.out.println("Again invalid input!");
        }

    }
}
