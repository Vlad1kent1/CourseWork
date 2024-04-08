import java.io.File
import java.util.Scanner

class CarParkingManager {
    companion object {
        private const val FILENAME = "car_parking_records.txt"
        private val records = mutableListOf<CarParkingRecord>()

        @JvmStatic
        fun main(args: Array<String>) {
            loadDataFromFile()
            val scanner = Scanner(System.`in`)

            while (true) {
                println("\nOptions:")
                println("1. Add Parking Record")
                println("2. View All Parking Records")
                println("3. Search by License Plate")
                println("4. Search by Owner's Phone")
                println("5. Filter by Parking Hour")
                println("6. Check Payment Status")
                println("7. Exit")
                print("Enter your choice: ")
                val choice = scanner.nextInt()
                scanner.nextLine()

                when (choice) {
                    1 -> addParkingRecord(scanner)
                    2 -> viewAllParkingRecords()
                    3 -> searchByLicensePlate(scanner)
                    4 -> searchByOwnerPhone(scanner)
                    5 -> filterByParkingHour(scanner)
                    6 -> checkPaymentStatus(scanner)
                    7 -> {
                        saveDataToFile()
                        println("Exiting...")
                        System.exit(0)
                    }
                    else -> println("Invalid choice. Please try again.")
                }
            }
        }

        private fun addParkingRecord(scanner: Scanner) {
            println("\nEnter Car Details:")
            print("Brand and Model: ")
            val brandModel = scanner.nextLine()
            print("License Plate: ")
            val licensePlate = scanner.nextLine()
            print("Owner's Phone: ")
            val ownerPhone = scanner.nextLine()
            print("Parking Hour: ")
            val parkingHour = scanner.nextInt()
            print("Prepaid Hours: ")
            val prepaidHours = scanner.nextInt()
            scanner.nextLine()

            val record = CarParkingRecord(brandModel, licensePlate, ownerPhone, parkingHour, prepaidHours)
            records.add(record)
            println("Parking record added successfully.")
        }

        private fun viewAllParkingRecords() {
            if (records.isEmpty()) {
                println("No parking records available.")
            } else {
                println("\nAll Parking Records:")
                records.forEach { println(it) }
            }
        }

        private fun searchByLicensePlate(scanner: Scanner) {
            print("\nEnter License Plate to search: ")
            val licensePlate = scanner.nextLine()
            val foundRecord = records.find { it.licensePlate.equals(licensePlate, ignoreCase = true) }
            if (foundRecord != null) {
                println("Matching Record: $foundRecord")
            } else {
                println("No matching record found.")
            }
        }

        private fun searchByOwnerPhone(scanner: Scanner) {
            print("\nEnter Owner's Phone to search: ")
            val ownerPhone = scanner.nextLine()
            val foundRecord = records.find { it.ownerPhone == ownerPhone }
            if (foundRecord != null) {
                println("Matching Record: $foundRecord")
            } else {
                println("No matching record found.")
            }
        }

        private fun filterByParkingHour(scanner: Scanner) {
            print("\nEnter Parking Hour to filter: ")
            val parkingHour = scanner.nextInt()
            val matchingRecords = records.filter { it.parkingHour == parkingHour }
            if (matchingRecords.isNotEmpty()) {
                println("Matching Records:")
                matchingRecords.forEach { println(it) }
            } else {
                println("No matching record found.")
            }
        }

        private fun checkPaymentStatus(scanner: Scanner) {
            print("\nEnter License Plate to check payment status: ")
            val licensePlate = scanner.nextLine()
            val foundRecord = records.find { it.licensePlate.equals(licensePlate, ignoreCase = true) }
            if (foundRecord != null) {
                val currentHour = getCurrentHour()
                val additionalHours = currentHour - foundRecord.parkingHour
                if (foundRecord.prepaidHours >= additionalHours) {
                    println("No additional payment required. Car can leave.")
                } else {
                    println("Additional payment required for $additionalHours hours.")
                }
            } else {
                println("No matching record found.")
            }
        }

        private fun getCurrentHour(): Int {
            return 10
        }

        private fun saveDataToFile() {
            try {
                val writer = File(FILENAME).printWriter()
                records.forEach { writer.println(it.toText()) }
                writer.close()
                println("Data saved successfully to file.")
            } catch (e: Exception) {
                println("Failed to save data to file: ${e.message}")
            }
        }

        private fun loadDataFromFile() {
            records.clear()
            try {
                val file = File(FILENAME)
                if (file.exists()) {
                    file.forEachLine { line ->
                        val record = CarParkingRecord.fromText(line)
                        record?.let { records.add(it) }
                    }
                    println("Data loaded successfully from file.")
                } else {
                    println("No existing data found. Starting with an empty record list.")
                }
            } catch (e: Exception) {
                println("Failed to load data from file: ${e.message}")
            }
        }
    }
}
