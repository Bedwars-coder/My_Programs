package com.company;

import java.util.Random;
import java.util.Scanner;

class GuessTheNumber {
    private int chances, boundTo, attempts = 1;
    // Getters and setters

    public int getChances() {
        return chances;
    }

    public void setChances(int chances) {
        this.chances = chances;
    }

    public int getBoundTo() {
        return boundTo;
    }

    public void setBoundTo(int boundTo) {
        this.boundTo = boundTo;
    }



    // Main code
    public void startGame(){
        Scanner sc = new Scanner(System.in);
        Random ran = new Random();
        try {
            int compChoice = ran.nextInt(boundTo + 1);
            while (attempts <= chances) {
                System.out.printf("Enter a number between 0 and %d\n", boundTo);
                int userChoice = sc.nextInt();
                if (userChoice > boundTo) {
                    System.out.println("You cannot enter a number greater than " + boundTo);
                    break;
                } else if (userChoice < compChoice) {
                    System.out.println("You entered a smaller number! Try again.");
                    System.out.println("Your used attempts: " + attempts);
                } else if (userChoice > compChoice) {
                    System.out.println("You entered a greater number! Try again.");
                    System.out.println("Your used attempts: " + attempts);
                } else if (userChoice == compChoice) {
                    System.out.println("Congratulations! You entered the correct number!");
                    System.out.println("You used " + attempts + " and won!");
                    break;
                }
                attempts++;
            }
            if (attempts > chances) {
                System.out.println("Alas! You lost. The correct number was " + compChoice);
            }
        } catch (Exception error1) {
            System.out.println("Not a valid input!");
        }
    }
}

public class GuessTheNumberOOPsEdition {
    public static void main(String[] args) {
        GuessTheNumber game = new GuessTheNumber();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of chances: ");
        int chances = sc.nextInt();
        game.setChances(chances);
        game.setBoundTo(100);
        game.startGame();
    }
}