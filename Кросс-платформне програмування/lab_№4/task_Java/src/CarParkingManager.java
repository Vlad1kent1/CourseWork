import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CarParkingManager {
    private static final String FILENAME = "car_parking_records.txt";
    private static final List<CarParkingRecord> records = new ArrayList<>();

    public static void main(String[] args) {
        loadDataFromFile();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nOptions:");
            System.out.println("1. Add Parking Record");
            System.out.println("2. View All Parking Records");
            System.out.println("3. Search by License Plate");
            System.out.println("4. Search by Owner's Phone");
            System.out.println("5. Filter by Parking Hour");
            System.out.println("6. Check Payment Status");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    addParkingRecord(scanner);
                    break;
                case 2:
                    viewAllParkingRecords();
                    break;
                case 3:
                    searchByLicensePlate(scanner);
                    break;
                case 4:
                    searchByOwnerPhone(scanner);
                    break;
                case 5:
                    filterByParkingHour(scanner);
                    break;
                case 6:
                    checkPaymentStatus(scanner);
                    break;
                case 7:
                    saveDataToFile();
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addParkingRecord(Scanner scanner) {
        System.out.println("\nEnter Car Details:");
        System.out.print("Brand and Model: ");
        String brandModel = scanner.nextLine();
        System.out.print("License Plate: ");
        String licensePlate = scanner.nextLine();
        System.out.print("Owner's Phone: ");
        String ownerPhone = scanner.nextLine();
        System.out.print("Parking Hour: ");
        int parkingHour = scanner.nextInt();
        System.out.print("Prepaid Hours: ");
        int prepaidHours = scanner.nextInt();
        scanner.nextLine();

        CarParkingRecord record = new CarParkingRecord(brandModel, licensePlate, ownerPhone, parkingHour, prepaidHours);
        records.add(record);
        System.out.println("Parking record added successfully.");
    }

    private static void viewAllParkingRecords() {
        if (records.isEmpty()) {
            System.out.println("No parking records available.");
        } else {
            System.out.println("\nAll Parking Records:");
            for (CarParkingRecord record : records) {
                System.out.println(record);
            }
        }
    }

    private static void searchByLicensePlate(Scanner scanner) {
        System.out.print("\nEnter License Plate to search: ");
        String licensePlate = scanner.nextLine();
        boolean found = false;

        for (CarParkingRecord record : records) {
            if (record != null && record.getLicensePlate().equalsIgnoreCase(licensePlate)) {
                System.out.println("Matching Record: " + record);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("No matching record found.");
        }
    }

    private static void searchByOwnerPhone(Scanner scanner) {
        System.out.print("\nEnter Owner's Phone to search: ");
        String ownerPhone = scanner.nextLine();
        boolean found = false;

        for (CarParkingRecord record : records) {
            if (record != null && record.getOwnerPhone().equals(ownerPhone)) {
                System.out.println("Matching Record: " + record);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("No matching record found.");
        }
    }

    private static void filterByParkingHour(Scanner scanner) {
        System.out.print("\nEnter Parking Hour to filter: ");
        int parkingHour = scanner.nextInt();
        boolean found = false;

        for (CarParkingRecord record : records) {
            if (record != null && record.getParkingHour() == parkingHour) {
                System.out.println("Matching Record: " + record);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No matching record found.");
        }
    }

    private static void checkPaymentStatus(Scanner scanner) {
        System.out.print("\nEnter License Plate to check payment status: ");
        String licensePlate = scanner.nextLine();
        boolean found = false;

        for (CarParkingRecord record : records) {
            if (record != null && record.getLicensePlate().equalsIgnoreCase(licensePlate)) {
                if (record.getPrepaidHours() >= (getCurrentHour() - record.getParkingHour())) {
                    System.out.println("No additional payment required. Car can leave.");
                } else {
                    System.out.println("Additional payment required for " + (getCurrentHour() - record.getParkingHour()) + " hours.");
                }
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("No matching record found.");
        }
    }

    private static int getCurrentHour() {
        return 10;
    }

    private static void saveDataToFile() {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILENAME))) {
            for (CarParkingRecord record : records) {
                if (record != null) {
                    writer.println(record.toText());
                }
            }
            System.out.println("Data saved successfully to file.");
        } catch (IOException e) {
            System.out.println("Failed to save data to file: " + e.getMessage());
        }
    }


    private static void loadDataFromFile() {
        records.clear();
        try (Scanner scanner = new Scanner(new FileReader(FILENAME))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                CarParkingRecord record = CarParkingRecord.fromText(line);
                records.add(record);
            }
            System.out.println("Data loaded successfully from file.");
        } catch (IOException e) {
            System.out.println("No existing data found. Starting with an empty record list.");
        }
    }
}
