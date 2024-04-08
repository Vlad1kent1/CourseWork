import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your number: ");
        int num = scanner.nextInt();

        int size = num / 1024;
        System.out.println("File size in kilobytes: " + size);

        scanner.close();
    }
}
