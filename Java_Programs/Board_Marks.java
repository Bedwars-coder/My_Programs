package com.company;
import java.util.Scanner;

public class Board_Marks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float sub1, sub2, sub3, sub4, sub5, cent, total_marks;
        try {
            System.out.println("Enter your marks in Physics");
            sub1 = sc.nextFloat();
            System.out.println("Enter your marks in Chemistry");
            sub2 = sc.nextFloat();
            System.out.println("Enter your marks in Computer");
            sub3 = sc.nextFloat();
            System.out.println("Enter your marks in Biology");
            sub4 = sc.nextFloat();
            System.out.println("Enter your marks in Mathematics");
            sub5 = sc.nextFloat();
            System.out.println("Enter the total marks of the five subjects");
            total_marks = sc.nextFloat();
            float temp = sub1 + sub2 + sub3 + sub4 + sub5;
            if (temp > total_marks) {
                System.out.format("Don't Underestimate me! I am very smart!\nYour total marks cannot exceed "+total_marks+"!");
            }
            else if (temp <= )

        } catch (Exception error1){
            System.out.println("You made something go wrong!");
        }
    }
}
