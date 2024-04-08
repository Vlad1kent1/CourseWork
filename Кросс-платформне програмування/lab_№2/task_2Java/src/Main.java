import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter values for coefficients a, b, and c:");
        System.out.print("a: ");
        double a = scanner.nextDouble();
        System.out.print("b: ");
        double b = scanner.nextDouble();
        System.out.print("c: ");
        double c = scanner.nextDouble();

        String solution = findSolution(a, b, c);

        System.out.printf("Solution to the inequality (x + %f)(x^2 - %f*x + %f) > 0:%n", a, b, c);
        System.out.println("Solution: " + solution);

        scanner.close();
    }

    public static String findSolution(double a, double b, double c) {
        double discriminant = b * b - 4 * c;
        if (discriminant < 0) {
            return "(" + (-a) + "; inf)";
        } else if (discriminant == 0) {
            double root = b / (2);
            if (-a > root)
                return "(" + (-a) + "; inf)";
            else if (-a < root)
                return "(" + (-a) + "; " + root + ")u(" + root + "; inf)";
            else if (-a == root)
                return "( -inf; " + root + ")u(" + root + "; inf)";
//            if (a < 0)
//                return (a >= root || 0 > root) ? "(0; inf)" : "(0; " + root + ")u(" + root + "; inf)";
//            else
//                if (-a > root)
//                    return "(" + (-a) + "; inf)";
//                else if (-a < root)
//                    return "(" + (-a) + "; " + root + ")u(" + root + "; inf)";
//                else
//                    return "(-inf; " + root + ")u(" + root + "; inf)";
            return "No solution!!!";
        } else {
            double root1 = (b - Math.sqrt(discriminant)) / (2);
            double root2 = (b + Math.sqrt(discriminant)) / (2);
            if (-a < root1)
                return "(" + (-a) + "; " + root1 + ")u(" + root2 + "; inf)";
            else if (-a > root1 && -a < root2)
                return "(" + root1 + "; " + (-a) + ")u(" + root2 + "; inf)";
            else if (-a > root2)
                return "(" + root1 + "; " + root2 + ")u(" + (-a) + "; inf)";
            else if (-a == root1 || -a == root2)
                return "(" + root2 + "; inf)";
//            if (a < 0) {
//                if (a >= root2)
//                    return "(0; inf)";
//                else if (a < root1)
//                    return "(0; " + root1 + ")u(" + root2 + "; inf)";
//                else if (a >= root1 && a < root2)
//                    return "(" + root2 + "; inf)";
//            } else {
//                if (-a > root2)
//                    return "(" + (-a) + "; inf)";
//                else if (-a < root1)
//                    return "(" + (-a) + "; " + root1 + ")u(" + root2 + "; inf)";
//                else
//                    return "(" + root2 + "; inf)";
//            }
            return "No solution!!!";
        }
    }
}
