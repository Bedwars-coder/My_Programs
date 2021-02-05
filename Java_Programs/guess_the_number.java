package com.company;

import java.util.Random;
import java.util.Scanner;

public class guess_the_number {
    public static void main(String[] args) {
        Random ran = new Random();
        Scanner sc = new Scanner(System.in);
        try {
            int random_no = ran.nextInt(101);
            System.out.println("You have ten attempts to guess the correct number less then 100!");
            int attempts = 0;
            while (attempts <= 9) {
                System.out.println("Enter a number less then 100!");
                int user_choice = sc.nextInt();
                if (user_choice > 100) {
                    System.out.printf("%d is greater than 100\n", user_choice);
                }
                else if (user_choice < random_no){
                    System.out.println("You entered a smaller number!");
                }
                else if (user_choice > random_no){
                    System.out.println("You entered a greater number!"); 
                }
                else if (user_choice == random_no){
                    System.out.println("You won!");
                    break;
                }
                attempts++;
            }
            if (attempts > 9){
                System.out.println("You lost!");
                System.out.printf("The number was %d", random_no);
            }
        } catch (Exception error1) {
            System.out.println("Again invalid input");
        }
    }
}
