import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] x = new int[4], y = new int[4];
        boolean flag = false;
        data_entry(x, y);
        checks(x, flag);
        checks(y, flag);

        do {
            System.out.println("Incorrected values were entered!!!");
            data_entry(x, y);
            checks(x, flag);
            checks(y, flag);
        } while(flag);
        System.out.println("Координати четвертої вершини прямокутника: (" + x[3] + ", " + y[3] + ")");
    }

    public static void data_entry(int[] x, int[] y){
        Scanner scanner = new Scanner(System.in);

        String[] str = {"A", "B", "C"};
        System.out.println("Enter the coordinates of the rectangle vertices");
        for (int i = 0; i < 3; i++) {
            System.out.printf("Vertex %s (x%d, y%d):%n", str[i], i + 1, i + 1);
            x[i] = scanner.nextInt();
            y[i] = scanner.nextInt();
        }
    }

    public static void checks(int[] a, boolean flag){
        if (a[0] == a[1])
            a[3] = a[2];
        else if (a[0] == a[2])
            a[3] = a[1];
        else if (a[1] == a[2])
            a[3] = a[0];
        else
            flag = true;
    }
}

