class CarParkingRecord {
    private String brandModel;
    private String licensePlate;
    private String ownerPhone;
    private int parkingHour;
    private int prepaidHours;

    public CarParkingRecord() {
        this.brandModel = "";
        this.licensePlate = "";
        this.ownerPhone = "";
        this.parkingHour = 0;
        this.prepaidHours = 0;
    }
    public CarParkingRecord(String brandModel, String licensePlate, String ownerPhone, int parkingHour, int prepaidHours) {
        this.brandModel = brandModel;
        this.licensePlate = licensePlate;
        this.ownerPhone = ownerPhone;
        this.parkingHour = parkingHour;
        this.prepaidHours = prepaidHours;
    }

    public String getBrandModel() {
        return brandModel;
    }

    public void setBrandModel(String brandModel) {
        this.brandModel = brandModel;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public void setLicensePlate(String licensePlate) {
        this.licensePlate = licensePlate;
    }

    public String getOwnerPhone() {
        return ownerPhone;
    }

    public void setOwnerPhone(String ownerPhone) {
        this.ownerPhone = ownerPhone;
    }

    public int getParkingHour() {
        return parkingHour;
    }

    public void setParkingHour(int parkingHour) {
        this.parkingHour = parkingHour;
    }

    public int getPrepaidHours() {
        return prepaidHours;
    }

    public void setPrepaidHours(int prepaidHours) {
        this.prepaidHours = prepaidHours;
    }

    @Override
    public String toString() {
        return "Car: " + brandModel + ", License Plate: " + licensePlate + ", Owner's Phone: " + ownerPhone +
                ", Parking Hour: " + parkingHour + ", Prepaid Hours: " + prepaidHours;
    }

    public String toText() {
        return brandModel + "," + licensePlate + "," + ownerPhone + "," + parkingHour + "," + prepaidHours;
    }

    public static CarParkingRecord fromText(String line) {
        String[] parts = line.split(",");
        if (parts.length == 5) {
            return new CarParkingRecord(parts[0], parts[1], parts[2], Integer.parseInt(parts[3]), Integer.parseInt(parts[4]));
        } else {
            return null;
        }
    }
}
