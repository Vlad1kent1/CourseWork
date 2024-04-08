import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter first number: ");
        double num1 = scanner.nextDouble();
        System.out.println("Enter second number: ");
        double num2 = scanner.nextDouble();

        double sum = Math.abs(num1) + Math.abs(num2);
        double difference = Math.abs(num1) - Math.abs(num2);
        double product = Math.abs(num1) * Math.abs(num2);
        double quotient = Math.abs(num1) / Math.abs(num2);

        System.out.println("Sum of modules: " + sum);
        System.out.println("Difference of modules: " + difference);
        System.out.println("Product of modules: " + product);
        System.out.println("Share of modules: " + quotient);

        scanner.close();
    }
}
