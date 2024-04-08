import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x, u, sum = 1, eps = 0.00001;
        System.out.print("Enter value x: ");
        x = scanner.nextDouble();
        u = -x/3;
        int n = 2;

        while (Math.abs(u) > eps) {
            sum += u;
            u *= -x * (3*n - 2) / (3*n);
            n++;
        }

        System.out.println("Sum value: " + sum);

        double libraryValue = Math.pow(1 + x, -1.0 / 3.0);
        System.out.println("Library function value: " + libraryValue);

        System.out.println("Number of terms: " + (n - 1));
    }
}
