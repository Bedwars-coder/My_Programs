package com.company;
import java.util.Random;
import java.util.Scanner;


public class Rock_paper_scissor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random ran = new Random();
        try{
            int attempts = 0;
            int user_points = 0;
            int comp_points = 0;
            while (attempts <= 9) {
                int random_no = ran.nextInt(3);
                System.out.println("Enter 0 for rock, 1 for paper or 2 for scissor: ");
                int user_choice = sc.nextInt();
                if (user_choice == 0 && random_no == 2 || user_choice == 1 && random_no == 0 || user_choice == 2 && random_no == 1) {
                    System.out.println("You won!");
                    user_points++;
                    System.out.printf("Computer's choice = %d", random_no);
                    System.out.println();
                    System.out.printf("Your points = %d", user_points);
                    System.out.println();
                    System.out.printf("Computer's points = %d", comp_points);
                    System.out.println();
                } else if (user_choice == random_no) {
                    System.out.println("Tie");
                    System.out.printf("Computer's choice = %d", random_no);
                } else if (user_choice == 2 && random_no == 0 || user_choice == 0 && random_no == 1 || user_choice == 1 && random_no == 2) {
                    System.out.println("You lost!");
                    System.out.printf("Computer's choice = %d", random_no);
                    comp_points++;
                }
                attempts++;
            }
        } catch (Exception error1){
            System.out.println("You made something go wrong!");
        }
    }
}
